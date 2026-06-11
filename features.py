# Jolify feautes file
# Required imports:
import os
import configuration
from storage import logAction

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def presetEighteenPlus():
    entries = [
        "127.0.0.1 pornhub.com",
        "127.0.0.1 www.pornhub.com",

        "127.0.0.1 xvideos.com",
        "127.0.0.1 www.xvideos.com",

        "127.0.0.1 xnxx.com",
        "127.0.0.1 www.xnxx.com",

        "127.0.0.1 redtube.com",
        "127.0.0.1 www.redtube.com",

        "127.0.0.1 youporn.com",
        "127.0.0.1 www.youporn.com",

        "127.0.0.1 xhamster.com",
        "127.0.0.1 www.xhamster.com",

        "127.0.0.1 spankbang.com",
        "127.0.0.1 www.spankbang.com",

        "127.0.0.1 brazzers.com",
        "127.0.0.1 www.brazzers.com",

        "127.0.0.1 tube8.com",
        "127.0.0.1 www.tube8.com",

        "127.0.0.1 rule34.com",
        "127.0.0.1 www.rule34.com",

        "127.0.0.1 erome.com",
        "127.0.0.1 www.erome.com",

        "127.0.0.1 onlyfans.com",
        "127.0.0.1 www.onlyfans.com\n"
    ]

    with open(configuration.sys32hosts, "r+") as f:
        content = f.read()
        for entry in entries:
            if entry not in content:
                f.write("\n# ADDED BY JOLIFY - 18+ filter\n" + entry + "\n")
    clear()
    print("\n18+ blocked succesfully!\n")
    logAction("18+ filter applied")

def presetSocialMedia():
    entries = [
        "127.0.0.1 instagram.com",
        "127.0.0.1 www.instagram.com",

        "127.0.0.1 tiktok.com",
        "127.0.0.1 www.tiktok.com",

        "127.0.0.1 facebook.com",
        "127.0.0.1 www.facebook.com",

        "127.0.0.1 x.com",
        "127.0.0.1 twitter.com",
        "127.0.0.1 www.x.com",
        "127.0.0.1 www.twitter.com",

        "127.0.0.1 reddit.com",
        "127.0.0.1 www.reddit.com",

        "127.0.0.1 tumblr.com",
        "127.0.0.1 www.tumblr.com",

        "127.0.0.1 9gag.com",
        "127.0.0.1 www.9gag.com",

        "127.0.0.1 snapchat.com",
        "127.0.0.1 www.snapchat.com\n"
    ]

    with open(configuration.sys32hosts, "r+") as f:
        content = f.read()
        for entry in entries:
            if entry not in content:
                f.write("\n# ADDED BY JOLIFY - Social Media filter\n" + entry + "\n")
    clear()
    print("\nSocial Media blocked succesfully!\n")
    logAction("Social Media filter applied")
    
    #functions for menu items
def functionOne():
    
        
        while True:
            clear()
            isAdded = False
            site = input("\nEnter website (example.com): ").strip()

            entries = [
                f"127.0.0.1 {site}",
                f"127.0.0.1 www.{site}"
            ]

            with open(configuration.sys32hosts, "r") as f:
                lines = f.readlines()
                newLines = []
                for line in lines:
                    if line.strip() not in entries:
                        newLines.append(line)
                    else:
                        clear()
                        print(f"{site} is already blocked!")
                        isAdded = True
                        break

                if isAdded == False:
                    with open(configuration.sys32hosts, "w") as f:
                        f.writelines(newLines)
                        f.write("\n# ADDED BY JOLIFY\n")
                        for entry in entries:
                            f.write(entry + "\n")
                
               
                            
                clear()
                print(f"\n{site} has been blocked succesfully!")
                logAction(f"Site blocked: {site}")
                blockMore = input("Block another site?: [y][n]").lower().strip()
                if blockMore == "n" or blockMore == "no":
                    clear()
                    break

def functionFive():
            clear()
            unblockSite = input("\nEnter website to unblock (example.com): ").strip()

            entries = [
                f"127.0.0.1 {unblockSite}",
                f"127.0.0.1 www.{unblockSite}"
            ]

            with open(configuration.sys32hosts, "r") as f:
                lines = f.readlines()
                newLines = []

                for line in lines:
                    if line.strip() not in entries:
                        newLines.append(line)

                clear()
                print(f"\n{unblockSite} has been unblocked succesfully!\n")
                logAction(f"Site unblocked: {unblockSite}")
            with open(configuration.sys32hosts, "w") as f:
                f.writelines(newLines)

def functionSix():
            
            while True:
                clear()
                isAdded = False
                print("\nINFORMATION: With this option you can reroute your router IP or your Nas IP to a custom website.\nBeware that this is only avaible only on your local computer and doesnt create a new domain entry in the world wide web")
                IPInput = input("Enter your Router/NAS/etc IP (for example: 192.168.1.1): ").strip()
                print("")
                siteOutput = input("Enter desired name (for example: MyRouter.com): ").strip()
                
                entries = [
                    f"{IPInput} {siteOutput}",
                    f"{IPInput} www.{siteOutput}"
                ]

                clear()
                with open(configuration.sys32hosts, "r") as f:
                    lines = f.readlines()
                    newLines = []
                    for line in lines:
                        if line.strip() not in entries:
                            newLines.append(line)
                            
                            
                            
                        else:
                            clear()
                            print(f"This connection is already mapped!")
                            isAdded = True
                            break;

                    if isAdded == False:
                        with open(configuration.sys32hosts, "w") as f:
                            f.writelines(newLines)
                            f.write("\n# ADDED BY JOLIFY - Custom IP mapping\n")
                            for entry in entries:
                                f.write(entry + "\n")
                        logAction(f"Custom IP mapping: {IPInput} -> {siteOutput}")
                        print(f"\nIP mapped successfully!")
               
                            
         
                
                
                mapMore = input("Map another IP?: [y][n]").lower().strip()
                if mapMore == "n" or mapMore == "n":
                    clear()
                    break

def functionSeven():
            clear()
            deleteEntries = input("\nAre you sure you want to reset your hosts file? This will remove ALL entries: [y][n]").lower().strip()
            print("")
            if deleteEntries == "y" or deleteEntries == "yes":
                with open(configuration.sys32hosts, "w") as f:
                    f.write("HOST FILE CLEARED BY JOLIFY\n\n# This file contains the mappings of IP addresses to host names.\n# Each entry should be kept on an individual line. \n# The IP address should be placed in the first column followed by the corresponding host name.\n# The IP address and the host name should be separated by at least one space.\n# Additionally, comments (such as these) may be inserted on individual lines or following the machine name denoted by a '#' symbol.\n")
                    logAction("Hosts file reset")
                clear()
                print("Hosts file reset successfully!\n")

def functionEight():
    clear()
    doesFileExist = False
    usernameUser = os.getlogin()

    mode = input("\nDo you want to create or upload a backup? (create/upload)[c][u]]").lower().strip()
    if mode == "create" or mode == "c":
         
        print("")
        backupName = input("Enter the name you want to give your backup file (without extension): ").strip()
        with open(configuration.sys32hosts, "r") as f:
             content = f.read()
               
        with open(fr"{configuration.jolifyBackupsPath}\{backupName}.txt", "w") as backupFile:
            backupFile.write(content)
            clear()
            print(f"\nBackup created successfully in the Jolify folder as {backupName}.txt\n")
        logAction(f"Backup created: {backupName}.txt")

    elif mode == "upload":
         while not doesFileExist:
            try:
                 print("")
                 backupPath = input(r"Enter the full path of the backup file you want to upload (for example: C:\Users\name\Desktop\backup.txt): ").strip()
                 backupPath = backupPath.replace('"', '')       
                 with open(backupPath, "r") as backupfile:
                     backupContent = backupfile.read()
                     with open(configuration.sys32hosts, "w") as f:
                        f.write(backupContent)
                 clear()
                 print("\nBackup uploaded successfully!\n")
                 logAction("Backup uploaded: " + backupPath)
                 doesFileExist = True
            except:
                    print("File not found, please try again.")


def functionNine():
            clear()
            print("\nFor customer support, please contact me at: maxim.kohanov@protonmail.com \nFor bug reports, please create an issue on the GitHub repository: https://github.com/OrthBoi/jolify\n")