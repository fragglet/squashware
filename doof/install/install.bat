@echo off
DEICE.EXE
if ERRORLEVEL == 1 GOTO END
DOOF.EXE
if ERRORLEVEL == 1 GOTO ERROR
DEL DOOF.EXE
FDSETUP
goto END
:ERROR
echo Error installing DOOF.EXE!
:END

