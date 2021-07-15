import threading
from tkinter import *
from threading import *
from bot_functions import *
from other_functions import *
from psutil import process_iter

# CREATES WINDOW OBJECT
root = Tk()

# GETS SCREEN DIMENSIONS
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# SETS WINDOW SIZE
root.geometry(f"800x600+{screen_width//2-400}+{screen_height//2-300}")

# DOES OTHER WINDOW SETUP
root.title("AFK Apex Bot")
root.iconbitmap("ApexPredators_Logo.ico")
root.configure(background='white')

# CREATES ALL THE LABELS AND ADDS THEM TO THE WINDOW
title_label = Label(root, text="Apex AFK Bot", background="white", font=("Helvetica", 30, "bold"))
label1 = Label(root, text="What is your resolution in Apex?", background="white", font=("Helvetica", 15, "bold"))
label2 = Label(root, text="(defaults to your monitor's revolution)", background="white", font=("Helvetica", 15, "bold"))
label3 = Label(root, text="What mode do you want to AFK in?", background="white", font=("Helvetica", 15, "bold"))
label4 = Label(root, text="", background="white", foreground="#ff4c4c", font=("Helvetica", 15, "bold"))
title_label.place(relx=.5, rely=.075, anchor="center")
label1.place(relx=.5, rely=.225, anchor="center")
label2.place(relx=.5, rely=.3, anchor="center")
label3.place(relx=.5, rely=.6, anchor="center")
label4.place(relx=.5, rely=.535, anchor="center")

# GET ALL OF THE IMAGES FOR THE BUTTONS
image1 = PhotoImage(file="button1.png")
image2 = PhotoImage(file="button2.png")
image3 = PhotoImage(file="button3.png")
image4 = PhotoImage(file="button4.png")
image5 = PhotoImage(file="button5.png")
image5_2 = PhotoImage(file="button5_2.png")
image1_pressed = PhotoImage(file="button1_pressed.png")
image2_pressed = PhotoImage(file="button2_pressed.png")
image3_pressed = PhotoImage(file="button3_pressed.png")
image4_pressed = PhotoImage(file="button4_pressed.png")
image5_pressed = PhotoImage(file="button5_pressed.png")
image5_2_pressed = PhotoImage(file="button5_2_pressed.png")

# CREATES TEXT FIELDS FOR KEYBINDS
entry1 = create_custom_entry(root=root, placeholder_text="Enter your interact key (Defaults to E)")
entry2 = create_custom_entry(root=root, placeholder_text="Enter your tactical key (Defaults to Q)")

# VARIABLES THAT ARE USED TO DETERMINE WHAT BUTTON IS PRESSED
res_button_pressed = ""
mode_button_pressed = 0
start_pressed = 0

# VARIABLE USED WHEN THE START BUTTON IS PRESSED TO KEEP TRACK OF IF THE BOT IS RUNNING OR IF THE USER NEEDS TO DO SOMETHING
running = False


# DEFINES THE FUNCTIONS THAT DETERMINE WHAT HAPPENS WHEN A BUTTON IS PRESSED
# HEXCODE OF UNPRESSED BUTTON IS #ff4c4c
# HEXCODE OF PRESSED BUTTON IS #ff7e7e
def button1_pressed():
    button1.configure(image=image1_pressed)
    button2.configure(image=image2)
    global res_button_pressed
    res_button_pressed = "HD"
    print("Resolution is set to 1080p")


def button2_pressed():
    button2.configure(image=image2_pressed)
    button1.configure(image=image1)
    global res_button_pressed
    res_button_pressed = "2K"
    print("Resolution is set to 1440p")


def button3_pressed():
    button3.configure(image=image3_pressed)
    button4.configure(image=image4)
    global mode_button_pressed
    mode_button_pressed = 3
    print("Mode is set to KD Lowering")
    entry1.place(relx=.5, rely=.75, anchor="center")
    entry2.place(relx=.5, rely=.8, anchor="center")
    label3.place(relx=.5, rely=.57, anchor="center")
    label4.place(relx=.5, rely=.515, anchor="center")
    button3.place(relx=.35, rely=.655, anchor="center")
    button4.place(relx=.65, rely=.655, anchor="center")


def button4_pressed():
    button4.configure(image=image4_pressed)
    button3.configure(image=image3)
    global mode_button_pressed
    mode_button_pressed = 4
    print("Mode is set to XP Grinding")
    # RETURNS THE GUI TO DEFAULT - WON'T APPEAR DIFFERENT UNLESS BUTTON 3 WAS PRESSED BEFORE
    label1.place(relx=.5, rely=.225, anchor="center")
    label2.place(relx=.5, rely=.3, anchor="center")
    label3.place(relx=.5, rely=.6, anchor="center")
    label4.place(relx=.5, rely=.535, anchor="center")
    button1.place(relx=.35, rely=.425, anchor="center")
    button2.place(relx=.65, rely=.425, anchor="center")
    button3.place(relx=.35, rely=.725, anchor="center")
    button4.place(relx=.65, rely=.725, anchor="center")
    button5.place(relx=.5, rely=.9, anchor="center")
    entry1.place_forget()
    entry2.place_forget()


def button5_pressed():
    # CREATING AND STARTING THE THREAD FOR THE BOT
    t1 = Thread(target=afk_bot_start)
    t1.start()


def afk_bot_start():
    # USED TO DETERMINE IF THE BOT IS RUNNING
    global running
    running = not running
    # CHECKS IF THE BOT IS ALLOWED TO RUN (USER HAS TO INPUT THINGS CORRECTLY)
    if res_button_pressed == "" or mode_button_pressed == 0:
        label4.configure(text="You must select the mode and resolution.")
        running = False
    elif mode_button_pressed == 3 and (len(entry1.get()) > 1 and entry1.get() != entry1.placeholder) or (len(entry2.get()) > 1 and entry2.get() != entry2.placeholder):
        label4.configure(text="You can only enter one character.")
        running = not running
    elif running:
        label4.configure(text="")
        button5.configure(image=image5_pressed)
        print("Launching bot")
        root.after(1000, button5.configure(image=image5_2))
        apex_bot = ApexBot(res_button_pressed)
        while True:
            if not running:
                break
            # CHECKS THROUGH THE PROCESSES RUNNING ON THE USER'S COMPUTER TO MAKE SURE APEX IS OPEN
            if "r5apex.exe" in [p.name() for p in process_iter()]:
                if mode_button_pressed == 4:
                    apex_bot.xp_grinding()
                else:
                    # GETS THE VALUES IN THE TEXT FIELDS
                    interact = entry1.get()
                    tactical = entry2.get()
                    # CHECKS TO SEE IF THE USER INPUTTED NOTHING, AND IF SO USES THE DEFAULT KEYS
                    if entry1.get() == entry1.placeholder:
                        interact = "e"
                    if entry2.get() == entry2.placeholder:
                        tactical = "q"
                    apex_bot.kd_lowering(interact_key=interact.lower(), tactical_key=tactical.lower())
    else:
        button5.configure(image=image5_2_pressed)
        print("Closing bot")
        root.after(1000, button5.configure(image=image5))


# CREATES ALL THE BUTTONS AND ADDS THEM TO THE WINDOW
button1 = Button(root, image=image1, borderwidth=0, foreground="white", command=button1_pressed)
button2 = Button(root, image=image2, borderwidth=0, foreground="white", command=button2_pressed)
button3 = Button(root, image=image3, borderwidth=0, foreground="white", command=button3_pressed)
button4 = Button(root, image=image4, borderwidth=0, foreground="white", command=button4_pressed)
button5 = Button(root, image=image5, borderwidth=0, foreground="white", command=button5_pressed)
button1.place(relx=.35, rely=.425, anchor="center")
button2.place(relx=.65, rely=.425, anchor="center")
button3.place(relx=.35, rely=.725, anchor="center")
button4.place(relx=.65, rely=.725, anchor="center")
button5.place(relx=.5, rely=.9, anchor="center")

# NEEDED FOR THE GUI TO APPEAR
root.mainloop()
