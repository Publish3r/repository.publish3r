@echo off
cls
cd %~dp0
7z.exe e -o%~dp0 %~dp0/download/temp/*.gz
exit
