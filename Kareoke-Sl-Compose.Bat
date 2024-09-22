:: Script: .\karaoke_sl_compose.bat

@echo off

:: Global List of Required Python Libraries
set LIBRARIES=pulsectl vlc PyGObject pyyaml

:: Global Variables for Pre-Launch
set DISTRO=

:: Read current distro from persistence.txt
call :read_persistence

:menu
cls
echo = * 120
echo     Kareoke-Sl-Compose
echo = * 120
echo.
echo     1. Run Kareoke-Sl-Compose.
echo.
echo     2. Change Linux Distro Used.
echo.     (Currently Selected Distro: %DISTRO%)
echo.
echo     3. Setup and Installer.
echo.
echo = * 120
set /p option="Selection; Menu Options = 1-3, Exit Program = X: "

if "%option%" == "1" goto run_karaoke
if "%option%" == "2" goto change_distro
if "%option%" == "3" goto setup_installer
if /i "%option%" == "X" goto exit

:run_karaoke
cls
echo Running Kareoke-Sl-Compose on WSL2 with distro: %DISTRO%...
wsl -d %DISTRO% -- python3 ./karaoke_sl_compose.py
goto end

:change_distro
cls
echo = * 120
echo     Select Ubuntu Distro:
echo = * 120

:: List available WSL distros
for /f "tokens=*" %%i in ('wsl -l -q') do echo     %%i

echo.
set /p new_distro="Selection; Enter the distro name or press B to go back: "

if /i "%new_distro%" == "B" goto menu

:: Save the new distro to persistence.txt and set global variable
set DISTRO=%new_distro%
echo distro=%DISTRO% > .\data\persistence.txt
echo Distro changed to %DISTRO%.
pause
goto menu

:setup_installer
cls
echo = * 120
echo     Setup and Installer
echo = * 120
echo Updating pip3 and installing required libraries...
wsl -d %DISTRO% -- pip3 install --upgrade pip
wsl -d %DISTRO% -- pip3 install %LIBRARIES%
echo.
echo Installation complete. Press any key to return to the main menu.
pause
goto menu

:exit
cls
echo Exiting...
goto end

:end
exit

:: Function to read persistence.txt and set DISTRO variable
:read_persistence
for /f "tokens=2 delims==" %%i in (.\data\persistence.txt) do (
    set DISTRO=%%i
)
exit /b
