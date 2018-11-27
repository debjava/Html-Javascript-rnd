# ********************************************************************************
# Author  : Debadatta Mishra
# Purpose : Uninstallation of already deployed application in IBM WAS 7
# ********************************************************************************
# ************** START OF VARIABLES DECLARATION ******************
application_name = 'corebank-server-war';
# ************** END OF VARIABLES DECLARATION ******************

AdminApp.uninstall(application_name);
AdminConfig.save();