# Jolify main file

import os
import features
import configuration
import storage
from features import clear

sys32hosts = configuration.sys32hosts
version = configuration.version


def main():
    clear()
    print(f"\nWelcome to Jolify {version}, the all in one Host manager!\nWhen prompted for input, please answer with either 'y' or 'n'\n")
    
    if storage.isFirstStart():
        while True: 
            try:
                setUpFolder = input("Do you want to set up Jolify longterm with its own folder on your system?: [y][n]").lower().strip()
                if setUpFolder == "y" or setUpFolder == "yes":
                    storage.setupJolifyFolder()
                    print("Jolify folder set up successfully!\n")
                    break
            except:
                clear()
                print("Invalid input, try again\n")
    while True:

# Read current content of hosts file
        content = "Empty"
        with open(sys32hosts, "r") as f:
                    content = f.read()

        if not storage.isFirstStart():
            # Display menu with backup feature
            print("\n1. Block website's")
            print("2. Block major 18+ sites")
            print("3. Block Social Media")
            print("4. Show current content")
            print("5. Unblock a website")
            print("6. Custom IP mapping")
            print("7. Reset hosts file")
            print("8. Backup hosts file")
            print("9. Customer Support")
            print("10. Exit")
        else:
            # Display menu without backup feature, because Jolify folder is not set up yet, so backup cannot be created.
            print("1. Block website's")
            print("2. Block major 18+ sites")
            print("3. Block Social Media")
            print("4. Show current content")
            print("5. Unblock a website")
            print("6. Custom IP mapping")
            print("7. Reset hosts file")
            print("9. Customer Support")
            print("10. Exit")

# Most functions were put into features.py to keep main clean, only small functions are kept here for better readability.
        choice = input("Choose an option: ").strip()

        if choice == "1":
            features.functionOne()

        elif choice == "2":
            features.presetEighteenPlus()

        elif choice == "3":
            features.presetSocialMedia()

        elif choice == "4":
            clear()
            with open(sys32hosts, "r+") as f:
                    content = f.read()
            print(f"{content}" + "\n")

        elif choice == "5":
            features.functionFive()

        elif choice == "6":
            features.functionSix()

        elif choice == "7":
            features.functionSeven()

        elif choice == "8" and not storage.isFirstStart():
            features.functionEight()

        elif choice == "9":
            features.functionNine()

        elif choice == "10":
            break

        else:
            clear
            print("Invalid choice\n")


if __name__ == "__main__":
    main()