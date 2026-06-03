# Jolify storage file
import datetime
import os
import configuration
from pathlib import Path


def setupJolifyFolder():
    Path(Path.home()/"Jolify"/"backups").mkdir(parents=True, exist_ok=True)
    with open(configuration.jolifyLogPath, "w+") as f:
        f.write(f"[{datetime.datetime.now()}] Jolify logging initiated\n")
    
def logAction(message):
    with open(configuration.jolifyLogPath, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {message}\n")

def isFirstStart():
   if not configuration.jolifyFolderPath.exists():
       return True