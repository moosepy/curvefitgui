# A GUI for scicpy's curve_fit() function

![The GUI interface](/images/curvefitgui1.png) 

`curvefitgui` is a graphical interface to the non-linear curvefit function [curve_fit](https://docs.scipy.org/doc/scipy/reference/reference/generated/scipy.optimize.curve_fit.html?highlight=scipy%20optimize%20curve_fit#scipy.optimize.curve_fit) of the scipy.optimize package. Currently, only the Levenberg-Marquard optimizer is supported. 

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
`curve_fit_gui` accepts the following arguments:
- **`f`:** callable
        function that defines the fitfunction
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

## GUI interface
![The GUI interface](/images/curvefitgui1.png)    