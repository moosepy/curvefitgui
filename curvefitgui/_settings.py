from importlib import resources as _resources
import configparser
import matplotlib.font_manager as fm
import matplotlib as mpl





def default_font():
    """
    Get the default font family used by Matplotlib.

    Returns:
        str: The name of the default font family.
    """
    return mpl.rcParams['font.family'][0]

def is_font_available(font_name):
    """
    Check if a given font is available on the system and recognized by Matplotlib.

    Args:
        font_name (str): The name of the font to check.

    Returns:
        bool: True if the font is available, False otherwise.
    """
    available_fonts = [f.name for f in fm.fontManager.ttflist]
    return font_name in available_fonts

def get_font(font_name):
    """
    Return the specified font name if available; otherwise, return the default font.

    Args:
        font_name (str): The desired font name.

    Returns:
        str: The font name if available, otherwise the default font.
    """
    if is_font_available(font_name):
        return font_name
    else:
        return default_font()


_config = configparser.ConfigParser()
with _resources.path("curvefitgui", "config.txt") as _path:
    _config.read(str(_path))

settings = {}

# general
settings['MODEL_NUMPOINTS'] = int(_config['general']['numpoints'])
settings['SIGNIFICANT_DIGITS'] = int(_config['general']['significant_digits'])
settings['XERRORWARNING'] = _config.getboolean('general','show_x_error_warning')
settings['SORT_RESIDUALS'] = _config.getboolean('general','sort_residuals')
settings['FONT'] = get_font(_config['general']['font'])


# fitparameters
settings['CM_SIG_DIGITS'] = int(_config['fitparameter']['significant_digits'])
settings['CM_SIG_DIGITS_NO_ERROR'] = int(_config['fitparameter']['significant_digits_fixed'])

# reportview
settings['REPORT_FONT'] = get_font(_config['reportview']['font'])
settings['REPORT_SIZE'] = int(_config['reportview']['size'])

# ticklabels
settings['TICK_COLOR'] = _config['ticklabels']['color']
settings['TICK_FONT'] = get_font(_config['ticklabels']['font'])
settings['TICK_SIZE'] = int(_config['ticklabels']['size'])

# text
settings['TEXT_FONT'] = get_font(_config['text']['font'])
settings['TEXT_SIZE'] = int(_config['text']['size'])

# errorbars
settings['BAR_Y_COLOR'] = _config['errorbars']['y_bar_color']
settings['BAR_X_COLOR'] = _config['errorbars']['x_bar_color']
settings['BAR_Y_THICKNESS'] = int(_config['errorbars']['y_bar_thickness'])
settings['BAR_X_THICKNESS'] = int(_config['errorbars']['x_bar_thickness'])

# figure
settings['FIG_DPI'] = int(_config['figure']['dpi'])