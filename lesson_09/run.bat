@echo off

set results=./results
set rep_history=./final-report/history
set report=./final-report

if exist %results% rmdir /s /q %results% 2>nul
pytest --alluredir=%results%

if exist %rep_history% (
    xcopy %rep_history% %results%/history /E /I /Y >nul
)

if exist %report% rmdir /s /q %report% 2>nul
allure generate %results% -o %report%
allure open %report%