# Jolify 1.3.0 beta 🙈
## Python Application to block websites on a device*

## Technologies
<img align="left" width="30px" src="https://camo.githubusercontent.com/b024a703f6c1dc4fca503f2d8663b6c69e2f2b8473e6461c35ed1ebbb4d3eabc/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f64657669636f6e732f64657669636f6e406c61746573742f69636f6e732f707974686f6e2f707974686f6e2d6f726967696e616c2e737667" style="max-width: 100%;">
<br>

## Features:
- Block and unblock custom websites
- 18+ child safety preset**
- Social Media preset**
- Display current host file content
- Custom IP mapping for home router/NAS/etc use
- Reset of host file to blank template
- Backup creation and upload
- Folder structure for logs and backups
- Changelogs to monitor all changes with datetime
  
### Detailed description
Jolify is simple python application build with one goal in mind: Modify the host file in the Windows32 folder in all possible ways.
By modifying this file the user can manually "block" websites by forcing the computer to use the host file as a dns lookup.
This does not replace a network wide router website blocker and is device specific.

## Supported platforms:
Jolify has been developed and tested on Windows 11.
Based on the knowledge that the file path to the hosts file is the same on Windows 11,10 and 8, Jolify should work just fine on those platforms too.
Mac and Linux are not supported.

### How to build
To build Jolify yourself make sure python is installed, run <code>python --version</code>
<ul>
  <li>Clone the repo using<code>git clone https://github.com/OrthBoi/jolify.git</code></li>
  <li>Go into the repo</li>
  <li>Make sure PyInstaller is installed using <code>python -m pip install PyInstaller</code></li>
  <li>Inside the folder execute <code>python -m PyInstaller --uac-admin --onefile --icon=jolify.ico --name Jolify main.py</code></li>
  <li>Wait for it to finish then go into "dist" folder and click on "jolify.exe"</li>
</ul>

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

