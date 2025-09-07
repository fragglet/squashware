@echo off
CLS
ECHO Welcome to:
TYPE BANNER.TXT
ECHO Creating RAM disk with Doom installation, please wait...
ECHO.
SRDISK /V1 /E 2048
%SRDISK1%:
A:\DOOFINST.EXE
COPY A:\FDOOM.CFG FDOOM.CFG
ECHO.
ECHO Done, starting the game!
FDOOM
ECHO To enable sound, please run FDSETUP.
