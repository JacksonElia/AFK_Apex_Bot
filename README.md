![AFK Apex Bot Banner](https://user-images.githubusercontent.com/85963782/152089759-d1aa1bca-4fa6-4dcc-8bef-2eca6ae6ef48.png)
-
A program that allows the user to AFK in Apex Legends games in order to either lower their KD or get XP. This is especially useful for finishing the battlepass or getting an heirloom as it can get a substantial amount of XP in a short period of time. **Only works in 1080P and 1440P** (Your primary monitor for Apex has to be one of these resolutions, check quick fixes at the bottom for a work around.). Also, it is assummed that your jump key is space and your move forward key is w but allows you to choose your interact key and tactical key. 

# How to use it
Go to ![image](https://user-images.githubusercontent.com/85963782/150718639-bec6b20b-f788-4d28-9315-25d33103b6ca.png) and download the latest release's installer (should be an exe.) Once downloaded, run the installer and if a popup appears saying "Windows protected your PC", click `more info` then `Run anyway`. Click `next` on the installer (making a desktop shortcut is recommended) then click `install` and `finish`.

If everything worked properly, when you launch the application you should see this window:

![image](https://user-images.githubusercontent.com/85963782/165866845-4d1eaafe-0192-42ab-abe9-463e407521ec.png)

To start using the bot, click on your monitor's resolution, either `1080P` (Most common) or `1440P`, then choose your AFK mode.

**KD Lowering**

If you want the bot to focus primarily on lowering your KD and thus your MMR, click on the `KD Lowering` button. It will jump out of the dropship early and use either Gibraltar  or Horizon to make you as visible and easy to kill as possible while keeping you from being kicked. If you have different keybinds than default, enter them in the text boxes. Finally, open your Apex and click `start`. 

**XP Grinding**

If you want the bot to focus on gaining as much XP as possible, click on the `XP Grinding` button. It will jump out of the dropship at the end of the path and keep your from being kicked. Finally, open your Apex and click `start`.

# Important to Know
- **Keep your screen turned on while you are having the bot AFK, it works by mimicking a player, so you have to have Apex visible and fullscreen.**
- **If you interact with Apex while the bot is active, it might get stuck.**
- **Allow up to 30 seconds of having you Apex running in full screen for the bot to start.**
- **Your Apex has to be in mouse in keyboard mode. If parts of the menu have controller buttons shown instead of m/kb buttons shown, it can cause the bot not to work. If your Apex is in controller mode, a quick fix is to press a button on your keyboard, or to move your mouse a little.**

# Quick Fixes
- If your monitor is a different resolution and or aspect ratio than 1080P or 1440P, in apex you can change this in settings->`video`. Change your aspex ratio to 16:9 and resolution to `1920 x 1080` or `2560 x 1440`.

![image](https://user-images.githubusercontent.com/85963782/156895505-65d3171f-b8aa-4e27-b13c-f7fa1dd82245.png)

# Known Bugs
- Nothing as of right now, if you find one, raise an `issue`.

# Frameworks, Tools, and Libraries used
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [PyDirectInput](https://pypi.org/project/PyDirectInput/)

I made this with PyCharm.

MIT © [JacksonElia](https://github.com/JacksonElia)
