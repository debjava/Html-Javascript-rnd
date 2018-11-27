@echo off
echo.*********************************************************************************
echo.*                                      *
echo.*  Starting the ESA HTTP SERVICE       *
echo.*                                      *
echo.*                                      *
echo.*********************************************************************************
echo.

rem EDI : ESA DEVICE INTEGRATION
if exist %DIRNAME% goto CURRENT_DIR_SETTING
    
rem if not exist %DIRNAME% goto ENV_DIR_SETTING
        
:CURRENT_DIR_SETTING
echo current directory accessible   
set DIRNAME="%CD%"
    
echo %DIRNAME%

echo CURRENT DIRECTORY ::: %DIRNAME%

set PROGNAME=run.bat

rem set RUNJAR=%EDI_HOME%\atcesadevices.jar

if exist %DIRNAME% goto FOUND_RUN_JAR

echo @@@@@@@@@@@@@@@@ ERROR @@@@@@@@@@@@@@@@@@@@@@
echo Could not locate "%DIRNAME%". Please check that you are in the
echo right directory when running this script. There may be problem
echo with the access permission in the specified directory.
echo Please contact your System Administrator or IT Help Desk.
echo @@@@@@@@@@@@@@@@ ERROR @@@@@@@@@@@@@@@@@@@@@@

goto END


:FOUND_RUN_JAR
java -jar %DIRNAME%\testswing.jar
rem exit

:END
if "%NOPAUSE%" == "" pause

rem ***** OLD Code *******
rem java -jar atcesadevices.jar

rem if "%NOPAUSE%" == "" pause

