from cx_Freeze import setup, Executable

setup(
    name="GAME",
    version="0.1",
    description="the typical 'Hello, world!' script",
    executables=[Executable("GAME.py", base="Win32GUI")])
'''
TO CREATE EXE
----------------------
Run in the terminal:
python setup.py build
-----------------------
'''