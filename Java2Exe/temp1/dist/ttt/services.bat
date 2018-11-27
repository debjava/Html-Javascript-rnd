@echo off

set DIRNAME="%CD%"
set EDISERVICENAME=ESASERVICE
REM - set NSSMPATH ="%DIRNAME%\nssm-2.7\win32"
rem - set t = @"nssm-2.7\win32"
rem - echo. t1 : %t%
rem - echo NSSMPATH : ^ %DIRNAME%\%t%

REM - %NSSMPATH%\nssm install %EDISERVICENAME% "C:\Documents and Settings\debadatta.m\Desktop\FinalDist\dist\runInv.exe" "C:\Documents and Settings\debadatta.m\Desktop\FinalDist\dist"
%DIRNAME%\nssm-2.7\win32\nssm install %EDISERVICENAME% %DIRNAME%\runInv.exe %DIRNAME%

echo Service Created Successfully

sc start %EDISERVICENAME%

echo Service Started Successfully

Rem -set nssmPath = nssm-2.7\win32\nssm.exe

Rem - TYPE %t%

rem - set str=the cat in the hat
rem - echo. %str%


REM if "%NOPAUSE%" == "" pause
