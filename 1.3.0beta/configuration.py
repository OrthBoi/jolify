# Jolify configuration file
#requied imports
from pathlib import Path

# PATHS

# HOST FILE PATH
# Real path, besure to uncomment before deploying
sys32hosts = r"C:\Windows\System32\drivers\etc\hosts"

# Training path, besure to comment before deploying
# sys32hosts = r"C:\Users\maxim\Desktop\jolify\testhosts.txt"

# JOLIFY FOLDER AND SUBPATHS
jolifyFolderPath = Path.home() / "Jolify"
jolifyLogPath = Path.home() / "Jolify" / "log.txt"
jolifyBackupsPath = Path.home() / "Jolify" / "backups"

version = "1.3.0beta"




