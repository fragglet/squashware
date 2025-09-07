@echo off
CLS
ECHO Welcome to:
TYPE BANNER.TXT
ECHO Creating RAM disk with Doom installation, please wait...
ECHO.
SRDISK /V1 /E 4096
%SRDISK1%:
COPY A:\DOOF.1 DOOFINST.EXE
DOOFINST
DEL DOOFINST.EXE
A:\SRDISK /V1 2048
COPY A:\FDOOM.CFG FDOOM.CFG
ECHO.
ECHO Done, starting the game!
FDOOM
ECHO To enable sound, please run FDSETUP.
