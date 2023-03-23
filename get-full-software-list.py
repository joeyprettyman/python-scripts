#====================================================
# IMPORTS
#====================================================
import os
import winreg
import logging


#====================================================
# CREATE THE DIRECTORY
#====================================================
# Get current user logon name
current_user        = os.getlogin()

# The new directory name will be <user>_backup
sub_directory       = os.getlogin() + "_backup"

# Root directory for sub directories to go inside of.
root_directory      = "backups"
full_path           = "./" + root_directory + "/" + sub_directory

# File information
software_file   = "Software-List.txt"
software_file   = full_path + "/" + software_file

# File to log software list to
logging.basicConfig( filename = software_file, filemode = "w", format = "%(message)s" )


#====================================================
# GET SOFTWARE LIST FROM REGISTRY
#====================================================
def getSoftware( hive, flag ):
    aReg = winreg.ConnectRegistry( None, hive )
    aKey = winreg.OpenKey( aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ | flag )

    count_subkey = winreg.QueryInfoKey( aKey )[0]

    software_list = []

    for i in range( count_subkey ):
        software = {}
        try:
            asubkey_name = winreg.EnumKey( aKey, i )
            asubkey      = winreg.OpenKey( aKey, asubkey_name )
            software['name'] = winreg.QueryValueEx( asubkey, "DisplayName" )[0]

            try:
                software['version'] = winreg.QueryValueEx( asubkey, "DisplayVersion" )[0]
            except EnvironmentError:
                software['version'] = "undefined"
            try:
                software['publisher'] = winreg.QueryValueEx( asubkey, "Publisher" )[0]
            except EnvironmentError:
                software['publisher'] = "undefined"
            software_list.append( software )
        except EnvironmentError:
            continue

    return software_list

software_list = getSoftware( winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + getSoftware( winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY ) + getSoftware( winreg.HKEY_CURRENT_USER, 0 )

for software in software_list:
    logging.warning( software['name'] + "\n" + "VERSION: " + software['version'] + "\n" + "PUBLISHER: " + software['publisher'] + "\n\n" )