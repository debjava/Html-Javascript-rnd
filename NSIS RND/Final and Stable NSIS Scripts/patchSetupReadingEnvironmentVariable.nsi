# Author : Debadatta Mishra

# Script developped by Debadatta Mishra

# It is a script for patch installation
# At the time of installation, no patch files
# will be displayed to the user.
# No uninstallation script is required for patch installation.
# It is also not required to write to the Windows registry.
# It is also not required to set the user menu group
# At the time of patch installation, it will read the environment
# variable to get the installation directory and finally it will
# install the necessary file/s in that location.
# It is always assumed that before running the patch installation,
# there is an installation in the system and environment variable
# has already been set.


Name "My Patch Application2"

# General Symbol Definitions
!define REGKEY "SOFTWARE\$(^Name)"
!define VERSION 1.1
!define COMPANY "Debadatta Mishra"
!define URL http://www.ddlab.com

# MUI Symbol Definitions
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install-colorful.ico"
!define MUI_FINISHPAGE_NOAUTOCLOSE
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall-colorful.ico"
!define MUI_UNFINISHPAGE_NOAUTOCLOSE

# FOR Environment variables setting
; Key - TEST_HOME Value - Installation Directory
!define ENV_VAR_NAME "TEST_HOME"
!define env_hklm 'HKLM "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"'
!define env_hkcu 'HKCU "Environment"'

# Included files
!include Sections.nsh
!include MUI2.nsh

# Installer pages
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

# Installer languages
!insertmacro MUI_LANGUAGE English

# Installer attributes
OutFile patchSetupReadingEnvironmentVariable.exe
InstallDir $PROGRAMFILES\MyApplication2
CRCCheck on
XPStyle on

; Never show the installation patch file details
; ShowInstDetails show
; Never show the list of patch files installed
ShowInstDetails nevershow

VIProductVersion 1.1.0.0
VIAddVersionKey ProductName "My Application2"
VIAddVersionKey ProductVersion "${VERSION}"
VIAddVersionKey CompanyName "${COMPANY}"
VIAddVersionKey CompanyWebsite "${URL}"
VIAddVersionKey FileVersion "${VERSION}"
VIAddVersionKey FileDescription ""
VIAddVersionKey LegalCopyright ""

# Installer sections
Section -Main SEC0000
	ReadEnvStr $R0 "${ENV_VAR_NAME}"
	SetOutPath $R0
    SetOverwrite on
    File /r patchexecutables\*
SectionEnd

# Installer functions
Function .onInit
    InitPluginsDir
FunctionEnd


