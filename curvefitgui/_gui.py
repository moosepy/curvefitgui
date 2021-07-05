# import the required packages
import warnings
import sys
from scipy.optimize import OptimizeWarning
from PyQt5 import QtCore, QtWidgets

from ._tools import Fitter, value_to_string
from ._widgets import PlotWidget, ModelWidget, ReportWidget
from ._settings import settings
from ._version import __version__ as CFGversion



class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, afitter, xlabel, ylabel):    
        super(MainWindow , self).__init__()
        
        # perform some initial default settings
        self.fitter = afitter
        self.xlabel, self.ylabel = xlabel, ylabel   
        self.output = (None, None)
        self.xerrorwarning = settings['XERRORWARNING']

        self.initGUI()
        
        self.plotwidget.update_plot()
        
       
    
    def closeEvent(self, event):
        """needed to properly quit when running in IPython console / Spyder IDE"""
        QtWidgets.QApplication.quit()
        

    def initGUI(self):
        # main GUI proprieties
        self.setGeometry(100, 100, 1415, 900)
        self.setWindowTitle(CFGversion)
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)

        # creating the required widgets
        self.plotwidget = PlotWidget(self.fitter.data, self.xlabel, self.ylabel)  # holds the plot
        self.modelview = ModelWidget(self.fitter.model, self.fitter.get_weightoptions())  # shows the model and allows users to set fitproperties
        self.fitbutton = QtWidgets.QPushButton('FIT', clicked = self.fit) 
        self.evalbutton = QtWidgets.QPushButton('EVALUATE', clicked = self.evaluate) 
        self.reportview = ReportWidget()  # shows the fitresults
        self.quitbutton = QtWidgets.QPushButton('QUIT', clicked = self.close)

        # create a layout for the buttons
        self.buttons = QtWidgets.QGroupBox()
        buttonslayout = QtWidgets.QHBoxLayout()
        buttonslayout.addWidget(self.evalbutton)
        buttonslayout.addWidget(self.fitbutton)
        self.buttons.setLayout(buttonslayout)

        # create a frame with a vertical layout to organize the modelview, fitbutton and reportview
        self.fitcontrolframe = QtWidgets.QGroupBox()
        fitcontrollayout = QtWidgets.QVBoxLayout()
        for widget in (self.modelview, self.buttons, self.reportview, self.quitbutton):
            fitcontrollayout.addWidget(widget)
        self.fitcontrolframe.setLayout(fitcontrollayout)
        
        # putting it all together: Setup the main layout
        mainlayout = QtWidgets.QHBoxLayout(self._main)
        splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(self.plotwidget)
        splitter.addWidget(self.fitcontrolframe)
        mainlayout.addWidget(splitter)
                
      
    def showdialog(self, message, icon, info='', details=''):
        """ shows an info dialog """
        msg = QtWidgets.QMessageBox()
        if icon == 'critical': msg.setIcon(QtWidgets.QMessageBox.Critical)
        if icon == 'warning': msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(message)
        msg.setInformativeText(info)
        msg.setWindowTitle("Message")
        msg.setDetailedText(details)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def set_output(self, output):
        """output should be a tuple with variables that are returned when closing the app"""
        self.output = output

    def get_output(self):
        """allows to return the currently stored output of the app when closed"""
        return self.output

    def evaluate(self):
        """ updates the model and computes the model curve with the current parameter values """
        # update the modelvalues from userinput 
        try:
            self.modelview.read_values()
        except ValueError:
            self.showdialog('Not a valid input initial parameter values', 'critical')
            return None

        # evaluate
        self.reportview.update_report({})
        self.plotwidget.canvas.set_fitline(self.fitter.get_curve())
        self.plotwidget.canvas.set_residuals(self.fitter.get_residuals(check=False))
        self.plotwidget.canvas.disable_results_box()
        self.plotwidget.update_plot()
        

    def fit(self):
        """ updates the model performs the fit and updates the widgets with the results """
        # update the modelvalues from userinput 
        try:
            self.modelview.read_values()
        except ValueError:
            self.showdialog('Not a valid input initial parameter values', 'critical')
            return None
        
        # update fitrange 
        self.plotwidget.canvas.get_range()

        # show warning on xerror data
        if (self.fitter.data.xe is not None) and self.xerrorwarning:
            self.showdialog('The error in x is ignored in the fit!', 'warning')
            self.xerrorwarning = False

        # perform the fit
        with warnings.catch_warnings():
            warnings.simplefilter("error", OptimizeWarning)  # make sure the OptimizeWarning is raised as an exception
            try:
                fitpars, fitcov = self.fitter.fit()
            except (ValueError, RuntimeError, OptimizeWarning):
                self.showdialog(str(sys.exc_info()[1]), 'critical')

            else:
                # update output 
                self.set_output((fitpars, fitcov))

                # update the widgets
                self.modelview.update_values()
                self.reportview.update_report(self.fitter.get_report())
                self.plotwidget.canvas.set_fitline(self.fitter.get_fitcurve())
                self.plotwidget.canvas.set_residuals(self.fitter.get_residuals())
                self.plotwidget.canvas.set_results_box(self._get_result_box_text(), 2)
                self.plotwidget.update_plot() 

    def _get_result_box_text(self):
        text = 'Fit results:'
        text = text + '\n' + 'weight:' + self.fitter.model.weight
        for par in self.fitter.model.fitpars:
            n  = par.name
            v = par.value
            e = par.sigma
            f = par.fixed
            text = text + '\n' + value_to_string(n, v, e, f)    
        return text    

def execute_gui(f, xdata, ydata, xerr, yerr, p0, xlabel, ylabel,
                absolute_sigma, jac, showgui, **kwargs):   
    """
    helper function that executes the GUI with an instance of the fitter class 
    """

    afitter = Fitter(f, xdata, ydata, xerr, yerr, p0, absolute_sigma, jac,**kwargs)
    if not showgui:
        return afitter.fit()
    
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication([])
    else:
        app = QtWidgets.QApplication.instance() 

    MyApplication = MainWindow(afitter, xlabel, ylabel)
    MyApplication.show()
    app.exec_()  
    return MyApplication.get_output()
    
