#====================================================
# IMPORTS
#====================================================
import os
import simple_chalk


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

# If directory does not already exist, create it.
if not os.path.exists( full_path ):
    os.mkdir( full_path )