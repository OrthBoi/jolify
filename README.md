# Jolify 1.3.0 beta 🙈
## Python Application to block websites on a device*

Features:
- Block and unblock custom websites
- 18+ child safety preset**
- Social Media preset**
- Display current host file
- Custom IP mapping for home router/nas/etc use
- Clearing of host file
- Backup creation and upload
- Homefolder Folder structure
- Changelogs

## DOCUMENTATION
### Detailed description
Jolify is simple python application build with one goal in mind: Modify the host file in the Windows32 folder in all possible ways.
By modifying this file the user can manually "block" websites by forcing the computer to use the host file as a dns lookup.
This does not replace a network wide router website blocker and is device specific.

### How to build
To build Jolify yourself:
1. Pull the Repo
2. Make sure PyInstaller is installed using 'python -m pip install PyInstaller'
3. Go into the repo and execute 'python -m PyInstaller --uac-admin --onefile --icon=jolify.ico jolify.py'
4. Wait for it to finish then go into "dist" folder and click on "jolify.exe"

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

