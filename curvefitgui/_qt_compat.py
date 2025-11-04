"""
Qt compatibility layer for PyQt5/PyQt6
"""


try:
    from PyQt6 import QtWidgets, QtCore, QtGui
    from PyQt6.QtCore import Qt
    from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
    from PyQt6.QtGui import QAction

    QT_VERSION = 6

    # Helper function for exec
    def exec_dialog(dialog):
        return dialog.exec()
    
    def exec_app(app):
        return app.exec()
    
except ImportError:
    from PyQt5 import QtWidgets, QtCore, QtGui
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QAction
    
    QT_VERSION = 5

    # Helper function for exec
    def exec_dialog(dialog):
        return dialog.exec_()
    
    def exec_app(app):
        return app.exec_()