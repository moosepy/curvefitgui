import unittest
import curvefitgui
import numpy as np

xdata = np.array([1, 2, 3, 4, 5])
ydata = np.array([-3.5, -2.4, -1, 0.5, 1.8])
yerr = np.array([0.5, 0.4, 0.6, 0.5, 0.8])

def f(x, a, b):
    return a * x + b

class LinearFitTest(unittest.TestCase):

    def test_non_weighted(self):
        popt_target = np.array([ 1.35, -4.97])
        pcov_target = np.array([[ 0.00143333, -0.0043],[-0.0043, 0.01576667]])
        popt, pcov = curvefitgui.curve_fit_gui(f, xdata, ydata, showgui=False)
        np.testing.assert_array_almost_equal(popt, popt_target, err_msg='popt failed')
        np.testing.assert_array_almost_equal(pcov, pcov_target, err_msg='popt failed')

    def test_weighted_relative(self):
        popt_target = np.array([ 1.3534158,  -4.99203498])
        pcov_target = np.array([[ 0.0022136,  -0.00579241], [-0.00579241,  0.01870192]])
        popt, pcov = curvefitgui.curve_fit_gui(f, xdata, ydata, yerr=yerr, showgui=False)
        np.testing.assert_array_almost_equal(popt, popt_target, err_msg='popt failed')
        np.testing.assert_array_almost_equal(pcov, pcov_target, err_msg='popt failed')  

    def test_weighted_standarddeviation(self):
        popt_target = np.array([ 1.3534158,  -4.99203498])
        pcov_target = np.array([[ 0.03359172, -0.08790064], [-0.08790064,  0.28380426]])
        popt, pcov = curvefitgui.curve_fit_gui(f, xdata, ydata, yerr=yerr, absolute_sigma=True, showgui=False)
        np.testing.assert_array_almost_equal(popt, popt_target, err_msg='popt failed')
        np.testing.assert_array_almost_equal(pcov, pcov_target, err_msg='popt failed')  


if __name__ == '__main__':
    unittest.main()