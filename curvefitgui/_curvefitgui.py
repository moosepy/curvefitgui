
import numpy as np
from ._gui import execute_gui


def linear_fit_gui(xdata, ydata, xerr=None, yerr=None, xlabel='x-axis', ylabel='y-axis', showgui=True):   
    """
    Graphical user interface for linear fitting
    
    Arguments:
    ----------
    xdata : 1-D numpy array
        x-coordinates of the data
    ydata : 1-D numpy array
        y-coordinates of the data
    yerr : 1-D numpy array, optional (default:None)
        error/uncertainty in y-values used for weighted fit 
        with a relative weight defined as 1/yerr**2  
        (for compatibility also the use of the keyword sigma can be used for the same)               
    xerr : 1-D numpy array, optional (default:None)
        error in x-values. For plotting errorbars only and ignored during fitting                      
    xlabel : string, optional (default:'x-values')
        x-axis title in the plot
    ylabel : string, optional (default:'y-values')
        y-axis title in the plot
    showgui : boolean, optional (default=True)
        if True, the gui is shown, otherwise not
        
    Returns:
    --------
    popt : numpy array
        optimal values for the fit parameters
    pcov : 2D numpy array
        the estimated covariance matrix op popt


    Notes:
    ------
    Not all functionality of curve_fit() is currently implemented. The solver is limited to the
    use of the Levenberg-Marquard algorithm. 

    Examples:
    ---------
        
        #define x and y data as 1 dimensional numpy arrays of equal length
        xdata = np.array([1,2,3,4,5])
        ydata = np.array([-3.5, -2.4, -1, 0.5, 1.8])
        
        #optinally define the errors in the ydata
        yerr = np.array([0.5,0.4,0.6,0.5,0.8])
        
        #optionally define axis titles
        xlabel = 'time / s'
        ylabel = 'height / m'
        
        #execute the function
        linear_fit_gui(xdata, ydata, yerr=yerr, xlabel=xlabel, ylabel=ylabel)
    
    """  

    # create fit function
    def f(x, a, b):
        """
        Linear fit
        y = ax + b
        a: slope
        b: intercept
        """
        return a * x + b

    p0=None
    absolute_sigma=False
    jac=None
    kwargs = {}
    
    res = execute_gui(f, xdata, ydata, xerr, yerr, p0, xlabel, ylabel,
                      absolute_sigma, jac, showgui, **kwargs)  
    return res


def curve_fit_gui(f, xdata, ydata, xerr=None, yerr=None,
                  p0=None, xlabel='x-axis', ylabel='y-axis',
                  absolute_sigma=False, jac=None, showgui=True,
                  **kwargs): 
    """
    Graphical user interface to the scipy curve_fit() function.
    
    Arguments:
    ----------
    f : callable
        function that defines the fitfunction
    xdata : 1-D numpy array
        x-coordinates of the data
    ydata : 1-D numpy array
        y-coordinates of the data
    yerr : 1-D numpy array, optional (default:None)
        error/uncertainty in y-values used for weighted fit 
        with a relative weight defined as 1/yerr**2  
        (for compatibility also the use of the keyword sigma can be used for the same)               
    xerr : 1-D numpy array, optional (default:None)
        error in x-values. For plotting errorbars only and ignored during fitting                      
    xlabel : string, optional (default:'x-values')
        x-axis title in the plot
    ylabel : string, optional (default:'y-values')
        y-axis title in the plot
    p0 : array-like, optional
        initial values for fit parameters, if not specified 1 is used for each parameter 
    showgui : boolean, optional (default=True)
        if True, the gui is shown, otherwise not
    absolute_sigma : boolean, optional
        see doc-string scipy.optimize.curve_fit() 
    jac : callable, optional
        see doc-string scipy.optimize.curve_fit() 
    kwargs
        keyword arguments for compatibility (e.g. you can use sigma to specify the error in y)
        

    Returns:
    --------
    popt : numpy array
        optimal values for the fit parameters
    pcov : 2D numpy array
        the estimated covariance matrix op popt

    See also:
    ---------
    scipy.optimize.curve_fit() 

    Notes:
    ------
    Not all functionality of curve_fit() is currently implemented. The solver is limited to the
    use of the Levenberg-Marquard algorithm. 

    Examples:
    ---------
    A minimum example is shown below

        #define a function for fitting
        def f(x, a, b):
            '''
            Linear fit
            function: y = ax + b
            a: slope
            b: intercept
            '''
            return a * x + b

        #define x and y data as 1 dimensional numpy arrays of equal length
        xdata = np.array([1, 2, 3, 4, 5])
        ydata = np.array([-3.5, -2.4, -1, 0.5, 1.8])
        
        #optinally define the errors in the ydata
        yerr = np.array([0.5, 0.4, 0.6, 0.5, 0.8])
        
        #optionally define axis titles
        xlabel = 'time / s'
        ylabel = 'height / m'
        
        #execute the function
        curve_fit_gui(f, xdata, ydata, yerr=yerr, xlabel=xlabel, ylabel=ylabel)
    
    """  
    # both keyword arguments 'sigma' and 'yerr' can be used to specify errors in the ydata
    # if 'sigma' is specified, 'yerr' is ignored.
    if 'sigma' in kwargs:
        yerr = kwargs['sigma']

    res = execute_gui(f, xdata, ydata, xerr, yerr, p0, xlabel, ylabel,
                      absolute_sigma, jac, showgui, **kwargs)
    return res
   

def __main__():
    # example of use and testing"
    print('Running curve_fit_gui() with some test data taken from scipy docs')

    # define fitfunction
    def func(x, a, b, c):
        """
        exponential decay
        function: a * exp(-b * x) + c
        a : amplitude
        b : rate
        c : offset
        """
        return a * np.exp(-b * x) + c

    # create test data
    xdata = np.linspace(0, 4, 50)
    y = func(xdata, 2.5, 1.3, 0.5)
    rng = np.random.default_rng()
    yerr = 0.2 * np.ones_like(xdata)
    y_noise = yerr * rng.normal(size=xdata.size)
    ydata = y + y_noise

    # execute the gui
    popt, pcov = curve_fit_gui(func, xdata, ydata, yerr=yerr, xlabel='x', ylabel='y')    
    print(f'popt = {popt}')
    print(f'pcov = {pcov}')
    
    print('Running linear_fit_gui() with some test data')
    #define x and y data as 1 dimensional numpy arrays of equal length
    xdata = np.array([2, 1, 3, 4, 5])
    ydata = np.array([-2.4, -3.5, -1, 0.5, 1.8])
        
    #optinally define the errors in the ydata and/or xdata
    yerr = np.array([0.5, 0.4, 0.6, 0.5, 0.8])
    xerr = np.array([0.1, 0.1, 0.1, 0.1, 0.1])
        
    #optionally define axis titles
    xlabel = 'time / s'
    ylabel = 'height / m'
        
    #execute the function
    popt, pcov = linear_fit_gui(xdata, ydata, xerr=xerr, yerr=yerr)  
    print(f'popt = {popt}')
    print(f'pcov = {pcov}')


if __name__ == "__main__":
    __main__()