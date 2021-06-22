import configparser


VERSION_INFO = 'curvefitgui versie 1.0.0'

config = configparser.ConfigParser()
config.read('config.txt')

# general
MODEL_NUMPOINTS = int(config['general']['numpoints'])
SIGNIFICANT_DIGITS = int(config['general']['significant_digits'])
XERRORWARNING = config.getboolean('general','show_x_error_warning')
SORT_RESIDUALS = config.getboolean('general','sort_residuals')
    
# fitparameters
CM_SIG_DIGITS = int(config['fitparameter']['significant_digits'])
CM_SIG_DIGITS_NO_ERROR = int(config['fitparameter']['significant_digits_fixed'])

# reportview
REPORT_FONT = config['reportview']['font']
REPORT_SIZE = int(config['reportview']['size'])

# ticklabels
TICK_COLOR = config['ticklabels']['color']
TICK_FONT = config['ticklabels']['font']
TICK_SIZE = int(config['ticklabels']['size'])

# text
TEXT_FONT = config['text']['font']
TEXT_SIZE = int(config['text']['size'])

# errorbars
BAR_Y_COLOR = config['errorbars']['y_bar_color']
BAR_X_COLOR = config['errorbars']['x_bar_color']
BAR_Y_THICKNESS = int(config['errorbars']['y_bar_thickness'])
BAR_X_THICKNESS = int(config['errorbars']['x_bar_thickness'])

