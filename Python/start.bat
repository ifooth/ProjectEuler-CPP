@echo off
cls
cd src
set i=1

:start
set /p input=Console %i%:
if "%input%"=="1" goto run

:run
"D:\Program Files\Python33\python.exe" _euler.py
set /a i+=1
goto start