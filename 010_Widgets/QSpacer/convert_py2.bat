@echo off

set PATH=%PATH%;C:\Users\yamagishi\AppData\Roaming\Python\Python37\Scripts
pyside2-uic -o hspacer_exp01_ui.py hspacer_exp01_ui.ui
pyside2-uic -o vspacer_exp01_ui.py vspacer_exp01_ui.ui

@REM pause