@echo off
echo.*********************************************************************************
echo.*                                      *
echo.*  Please wait..................       *
echo.*                                      *
echo.*                                      *
echo.*********************************************************************************
echo.


set DIRNAME="%CD%"

echo CURRENT DIRECTORY ::: %DIRNAME%

set PROGNAME=test.bat


java -jar %DIRNAME%\testswing.jar

if "%NOPAUSE%" == "" pause



