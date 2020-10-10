@echo off
cls
cd %~dp0
7z.exe e -o%~dp0/download %~dp0/download/*.xz
exit