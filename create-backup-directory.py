import os

current_user = os.getlogin()
sub_directory = current_user + "_backup"
root_directory = "backups"
full_path = os.path.join(".", root_directory, sub_directory)

try:
    os.makedirs(full_path)
    print(f"Backup directory created at {full_path}")
except OSError as error:
    print(f"Error creating backup directory: {error}")