@echo off

cd %CM_RUN_DIR%

echo %CM_RUN_CMD%
pause

%CM_RUN_CMD%

IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%
