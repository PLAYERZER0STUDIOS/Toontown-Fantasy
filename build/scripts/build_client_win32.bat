@echo off
title Toontown Fantasy Builder
cd ..
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64 %*
"C:\Open-Panda\python\python.exe" -m src.make
PAUSE