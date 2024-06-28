import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

exec(open('./curvefitgui/_version.py').read())

# This call to setup() does all the work
setup(
    name="curvefitgui",
    version=__version__,
    description="GUI for the scipy.optimize.curve_fit() function",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/moosepy/curvefitgui", 
    author="moosepy",
    author_email="moose_dev@icloud.com", 
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7, <4',
    packages=["curvefitgui"],
    include_package_data=True,
    package_data={
      'curvefitgui': ['config.txt'],
    },
    install_requires=[
        "matplotlib",
        "numpy",
        "scipy",
        # PyQt6 and PySide6 are not included here by purpose, to let the user
        # choose which backend to use. PyQt5 or PySide2 are not supported.
    ],
)
