import cx_Freeze
import sys
import os

# Include TK Libs
os.environ['TCL_LIBRARY'] = r'C:\\Users\\KeyShout\\AppData\\Local\\Programs\\Python\\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\\Users\\KeyShout\\AppData\\Local\\Programs\\Python\\Python36\tcl\tk8.6'

executables = [
    cx_Freeze.Executable( 
        script="main.py",
        base = "Win32GUI"
    )
]

cx_Freeze.setup(
    name='Game of Hacker',
    options={'build_exe':{'packages':['tkinter'], 'include_files':[r'C:\Users\KeySHOUT\Desktop\GameOfHacker\img']}},
    executables = executables,
    version = '1.0.0'
)