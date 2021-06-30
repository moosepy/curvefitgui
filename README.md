# A GUI for scipy's curve_fit() function


![The GUI interface](/images/curvefitgui1.png) 

`curvefitgui` is a graphical interface to the non-linear curvefit function [scipy.optimise.curve_fit API reference](https://docs.scipy.org/doc/scipy/reference/reference/generated/scipy.optimize.curve_fit.html?highlight=scipy%20optimize%20curve_fit#scipy.optimize.curve_fit) of the scipy.optimize package. Currently, only the Levenberg-Marquard optimizer is supported. 

## Installation

You can install the `curvefitgui` form [PyPi](https://pypi.org/project/curvefitgui/):

    pip install curvefitgui

The GUI is supported on Python 3.7 and above.

## Basic usage
A minimum example to use `curvefitgui.curve_fit_gui` is:
```python
import curvefitgui as cfg
import numpy as np

# define a function for fitting
def f(x, a, b):
    '''
    Linear fit
    function: y = ax + b
    a: slope
    b: intercept
    '''
    return a * x + b

# define x and y data as 1 dimensional numpy arrays of equal length
xdata = np.array([1, 2, 3, 4, 5])
ydata = np.array([-3.5, -2.4, -1, 0.5, 1.8])
        
# execute the function
cfg.curve_fit_gui(f, xdata, ydata)   
```
## Arguments
```python
curve_fit_gui(f, xdata, ydata, xerr=None, yerr=None, p0=None, 
              xlabel='x-axis', ylabel='y-axis', absolute_sigma=False, 
              jac=None, showgui=True, **kwargs)
```

`curve_fit_gui` accepts the following arguments:
- **`f`:** callable
        function that defines the fitfunction. The first argument of `f` should be the independent variable; other arguments (at least one) are considered to be the fitparameters. 
- **`xdata`:** 1-D numpy array
        x-coordinates of the data
- **`ydata`:** 1-D numpy array
        y-coordinates of the data

`curve_fit_gui` accepts the following keyword 
arguments:        

- **`yerr`:** 1-D numpy array, optional (default:None)
        error/uncertainty in y-values used for weighted fit 
        with a relative weight defined as 1/yerr**2  
        (for compatibility also the use of the keyword sigma can be used for the same)               
- **`xerr`:** 1-D numpy array, optional (default:None)
        error in x-values. For plotting errorbars only and ignored during fitting                      
- **`xlabel`:** string, optional (default:'x-values')
        x-axis title in the plot
- **`ylabel`:** string, optional (default:'y-values')
        y-axis title in the plot
- **`p0`:** array-like, optional
        initial values for fit parameters, if not specified 1 is used for each parameter 
- **`showgui`:** boolean, optional (default=True)
        if True, the gui is shown, otherwise not
- **`absolute_sigma`:** boolean, optional
        see doc-string scipy.optimize.curve_fit() 
- **`jac`:** callable, optional
        see doc-string scipy.optimize.curve_fit() 
- **`kwargs`:**
        keyword arguments for compatibility (e.g. you can use sigma to specify the error in y)

## Returns
- **`popt`:** The values of the fitparameters that minimised the squared residuals if a succesful fit was performed, else *None*.
- **`pcov`:** The estimated covariance of popt. 
(see also: [scipy.optimise.curve_fit API reference](https://docs.scipy.org/doc/scipy/reference/reference/generated/scipy.optimize.curve_fit.html?highlight=scipy%20optimize%20curve_fit#scipy.optimize.curve_fit))

## GUI interface
Once the `gui` is executed the following window is visible. An explanation of the different controls is described below the figure.

![The GUI interface](/images/curvefitgui2.png)    

### GUI controls
1. **Data plot:** A matplotlib plot that shows the data as solid dots and both y-error and x-error errorbars if provided. A fitted curve as a dashed line is shown if a fit is performed.
2. **Residual plot** A matplotlib plot that shows the residuals as the difference between the measured and fitted values: `residual = ydata - f(xdata, *fitparameters)` 
3. **Model settings:** Here you can enter inital values for the fitparameters. By ticking the chcekbox `fix` you can set a parameter to fixed:e.g. the parameter is not optmised during the fit.
4. **Weight settings:** If error data on the y-values are passed using the keyword argument `yerr` you can use the dropdownbox to set how the error data is treated:
    - *None*: the error data is ignored
    - *Relative*: Use the error data for a relative weight. Corresponds to setting scipy's curve_fit() function keyword `absolute_sigma = False`.
    - *Standard deviation*: Treat the error data as being standard deviations. Corresponds to setting scipy's curve_fit() function keyword `absolute_sigma = True`.
5. **Evaluate:** Use this button to compute the model function given the current values of the parameters (set in the model settings panel)
6. **Fit:** Performs the fit and updates the parameter values.
7. **Report:** When a fit is performed, the results are shown here. The information on the model is actually the provided docstring of the function `f` that is passed to the `curvefitgui` function.
8. **Quit:** Quits the gui and returns the fitparameters `popt` and `pcov`.
9. **Toolbar:** This is the standard matplotlib toolbar to adjust some plot properties and provides zoom/pan and save options.
10. **FitTextbox:** This textbox is generated if a valid fit is performed. It can be moved by the mouse to any conveniant positions in the plot.
11. **Range Selector** Activates/deactivates the range-selector. The range-selector allows to select a datarange used for fitting. Only datapoints that are within the two vertical dashed lines are considered during fitting. The lines can be moved using the mouse.