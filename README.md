# AFK_Apex_Bot
A program that allows the user to AFK in Apex Legends games in order to either lower their KD or get XP. This is especially useful for finishing the battlepass or getting an heirloom as it can get a substantial amount of XP in a short period of time. **Only works in 1080P and 1440P** (Your primary monitor for Apex has to be one of these resolutions). Also, it is assummed that your jump key is space and your move forward key is w but allows you to choose your interact key and tactical key. **Additionally, your Apex has to be in mouse in keyboard mode. If parts of the menu have controller buttons shown instead of m/kb buttons shown, it can cause the bot not to work.** If your Apex is in controller mode, a quick fix is to press a button on your keyboard or to move your mouse a little.

# How to use it
Go to ![image](https://user-images.githubusercontent.com/85963782/150718639-bec6b20b-f788-4d28-9315-25d33103b6ca.png) and download the latest release's installer (should be an exe.) Once downloaded, run the installer and if a popup appears saying "Windows protected your PC", click `more info` then `Run anyway`. Click `next` on the installer (making a desktop shortcut is recommended) then click `install` and `finish`.

If everything worked properly, when you launch the application you should see this window:

![image](https://user-images.githubusercontent.com/85963782/150719005-7336ae4a-a10d-448a-9685-f751ce58c4c0.png)

To start using the bot, click on your monitor's resolution, either `1080P` (Most common) or `1440P`, then choose your AFK mode.

**KD Lowering**

If you want the bot to focus primarily on lowering your KD and thus your MMR, click on the `KD Lowering` button. It will jump out of the dropship early and use either Gibraltar  or Horizon to make you as visible and easy to kill as possible while keeping you from being kicked. If you have different keybinds than default, enter them in the text boxes. Finally, open your Apex and click `start`. 

**XP Grinding**

If you want the bot to focus on gaining as much XP as possible, click on the `XP Grinding` button. It will jump out of the dropship at the end of the path and keep your from being kicked. Finally, open your Apex and click `start`.

**Keep your screen on while you are having the bot AFK, it works by mimicking a player, so you have to have Apex visible and fullscreen.**
**If you interact with Apex while the bot is active, it might get stuck.**

# Frameworks, Tools, and Libraries used
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [PyDirectInput](https://pypi.org/project/PyDirectInput/)

I made this with PyCharm.

MIT © [Traptricker](https://github.com/Traptricker)
