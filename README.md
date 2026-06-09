# Jolify 1.3.0 beta 🙈
## Python Application to block websites on a device*

Features:
- Block and unblock custom websites
- 18+ child safety preset**
- Social Media preset**
- Display current host file content
- Custom IP mapping for home router/NAS/etc use
- Reset of host file to blank template
- Backup creation and upload
- Folder structure for logs and backups
- Changelogs to monitor all changes with datetime

## DOCUMENTATION
### Detailed description
Jolify is simple python application build with one goal in mind: Modify the host file in the Windows32 folder in all possible ways.
By modifying this file the user can manually "block" websites by forcing the computer to use the host file as a dns lookup.
This does not replace a network wide router website blocker and is device specific.

## Supported platforms:
Jolify has been developed and tested on Windows 11.
Based on the knowledge that the file path to the hosts file is the same on Windows 11,10 and 8, Jolify should work just fine on those platforms too.
Mac and Linux are not supported.

### How to build
To build Jolify yourself:
1. Download the current latest version
2. Open the folder in PowerShell
3. Make sure PyInstaller is installed using '''python -m pip install PyInstaller'''
4. Inside the folder execute '''python -m PyInstaller --uac-admin --onefile --icon=jolify.ico --name Jolify main.py'''
5. Wait for it to finish then go into "dist" folder and click on "jolify.exe"

### Use case
Want to make some website unreachable for a childs computer or maybe your router doesnt offer a simple domain to access it in your network?
With Jolify you can do exactly that! You dont need a website blocking app nore do you need to mess around with your router settings. 
The only thing you need is this one application (which you can even delete after use, the settings will be kept), even your grandma can use Jolify with ease!

### *Discplaimers
This is a personal learning project, you may use Jolify at your own risk.
*It isnt guarenteed that API's of Website's will get blocked. Websites will only get blocked on the devic you ran the app on
**The templates do not block all 18+ / Social Media apps, as it works using a predifined list. (feel free to add more sites using a pull request!)

Maxim Kohanov
02.06.2026

