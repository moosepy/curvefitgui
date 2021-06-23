import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="curvefitgui",
    version="1.0.0",
    description="GUI for the scipy.optimize.curve_fit() function",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kangercode/curvefitgui", 
    author="jskanger",
    author_email="kangerdev@icloud.com", 
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires='>=3.6, <4',
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
                        "matplotlib", 
                        "numpy",
                        "configparser",
                        "warnings"
                        "sys",
                        "scipy",
                        "PyQt5"
                        "inspect",
                        "dataclasses",
                        "typing"
    ], # need to check versions
    package_data={'curvefitgui': ['config.txt']} # check
    
)
