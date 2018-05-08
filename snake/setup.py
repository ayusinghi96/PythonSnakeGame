import os
os.environ['TCL_LIBRARY'] = r'C:\python3.6\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\python3.6\tcl\tk8.6'

import cx_Freeze

executables = [cx_Freeze.Executable("snake.py")]

cx_Freeze.setup(
    name = "Snake Game",
    options = {"build_exe":{"packages":["pygame"], "include_files":["snakehead.png","apple.png"]}},

    description = "snake game",
    executables = executables)
    
