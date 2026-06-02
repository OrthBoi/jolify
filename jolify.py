#ToDo: Take reused functions and put them in a seperate method, also put the diffrent menu items into methods to clean up main code.

import os


sys32hosts = r"C:\Windows\System32\drivers\etc\hosts"
# path for developement hostfile
#  r"C:\Users\maxim\Desktop\jolify\testhosts.txt"



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

    with open(sys32hosts, "r+") as f:
        content = f.read()
        for entry in entries:
            if entry not in content:
                f.write("\n# ADDED BY JOLIFY - 18+ filter\n" + entry)
    print("18+ blocked succesfully!\n")

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

    with open(sys32hosts, "r+") as f:
        content = f.read()
        for entry in entries:
            if entry not in content:
                f.write("\n# ADDED BY JOLIFY - Social Media filter\n" + entry)
    print("Social Media blocked succesfully!\n")


def main():
    
    print("Welcome to Jolify 1.2.0, the all in one Host manager!\n When prompted for input, please answer with either 'y' or 'n'\n")
    
    while True:

        content = "Empty"
        with open(sys32hosts, "r+") as f:
                    content = f.read()

        # Display menu
        print("1. Block website's")
        print("2. Block major 18+ sites")
        print("3. Block Social Media")
        print("4. Show current content")
        print("5. Unblock a website")
        print("6. Custom IP mapping")
        print("7. Reset hosts file")
        print("9. Customer Support")
        print("10. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("")
            while True:
                isAdded = False
                site = input("Enter website (example.com): ").strip()

                entries = [
                    f"127.0.0.1 {site}",
                    f"127.0.0.1 www.{site}"
                ]

                with open(sys32hosts, "r") as f:
                    lines = f.readlines()
                    newLines = []
                    for line in lines:
                        if line.strip() not in entries:
                            newLines.append(line)
                        else:
                            print(f"{site} is already blocked!")
                            isAdded = True

                    if isAdded == False:
                        with open(sys32hosts, "w") as f:
                            f.writelines(newLines)
                            f.write("\n# ADDED BY JOLIFY\n")
                            for entry in entries:
                                f.write(entry + "\n")
                
               
                            

                print(f"{site} has been blocked succesfully!")
                blockMore = input("Block another site?: ").lower().strip()
                if blockMore == "n" or blockMore == "n":
                    break

        elif choice == "2":
            print("")
            presetEighteenPlus()

        elif choice == "3":
            print("")
            presetSocialMedia()

        

        elif choice == "4":
            print("")
            print(f"{content}" + "\n")

        elif choice == "5":
            print("")
            unblockSite = input("Enter website to unblock (example.com): ").strip()

            entries = [
                f"127.0.0.1 {unblockSite}",
                f"127.0.0.1 www.{unblockSite}"
            ]

            with open(sys32hosts, "r") as f:
                lines = f.readlines()
                newLines = []

                for line in lines:
                    if line.strip() not in entries:
                        newLines.append(line)
                
                print(f"{unblockSite} has been unblocked succesfully!\n")

            with open(sys32hosts, "w") as f:
                f.writelines(newLines)

        elif choice == "6":
            print("")
            while True:
                isAdded = False
                print("INFORMATION: With this option you can reroute your router IP or your Nas IP to a custom website.\nBeware that this is only avaible only on your local computer and doesnt create a new domain entry in the world wide web")
                IPInput = input("Enter your Router/NAS/etc IP (for example: 192.168.1.1): ").strip()
                siteOutput = input("Enter desired name (for example: MyRouter.com): ").strip()
                
                entries = [
                    f"{siteOutput} {IPInput}",
                    f"{siteOutput} www.{IPInput}"
                ]

                with open(sys32hosts, "r") as f:
                    lines = f.readlines()
                    newLines = []
                    for line in lines:
                        if line.strip() not in entries:
                            newLines.append(line)
                        else:
                            print(f"This connection is already mapped!")
                            isAdded = True

                    if isAdded == False:
                        with open(sys32hosts, "w") as f:
                            f.writelines(newLines)
                            f.write("\n# ADDED BY JOLIFY - Custom IP mapping\n")
                            for entry in entries:
                                f.write(entry + "\n")
                
               
                            

                print(f"IP mapped successfully!")
                mapMore = input("Map another IP?: ").lower().strip()
                if mapMore == "n" or mapMore == "n":
                    break
             
        elif choice == "7":
            deleteEntries = input("Are you sure you want to reset your hosts file? This will remove ALL entries: ").lower().strip()
            print("")
            if deleteEntries == "y" or deleteEntries == "yes":
                with open(sys32hosts, "w") as f:
                    f.write("HOST FILE CLEARED BY JOLIFY\n\n# This file contains the mappings of IP addresses to host names.\n# Each entry should be kept on an individual line. \n# The IP address should be placed in the first column followed by the corresponding host name.\n# The IP address and the host name should be separated by at least one space.\n# Additionally, comments (such as these) may be inserted on individual lines or following the machine name denoted by a '#' symbol.\n")

        elif choice == "9":
            print("")
            print("For customer support, please contact me at: maxim.kohanov@protonmail.com \nFor bug reports, please create an issue on the GitHub repository: https://github.com/OrthBoi/jolify\n")

        elif choice == "10":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
