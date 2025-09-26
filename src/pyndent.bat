@echo off
set lastver=pyndent-0.1.0.0_20250925
REM
REM PYndent last stable version - The Python re-Indent Pre-processor
REM (C)2025 by Elwe Thor - Aria@DeepSeek - CC-BY-NC-SA 4.0
REM
%lastver%.py %*
if errorlevel 1 (
    echo.
    echo Pyndent completed with errors (RC=%errorlevel%)
    exit /b %errorlevel%
)
