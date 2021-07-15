import pyautogui
import pydirectinput
from time import sleep
from random import randint
from psutil import process_iter


def queue_into_game(resolution):
    # TRY STATEMENT MAKES SURE THE GAME DOESN'T CRASH IF ONE OF THE BUTTONS CAN'T BE FOUND
    try:
        if pyautogui.locateOnScreen(f"fill_teammates{resolution}.png", confidence=.95) is not None:
            fill_button_cords = pyautogui.center(pyautogui.locateOnScreen(f"fill_teammates{resolution}.png", confidence=.8))
            pydirectinput.click(fill_button_cords.x, fill_button_cords.y)
        sleep(1)
        ready_button_cords = pyautogui.center(pyautogui.locateOnScreen(f"ready_button{resolution}.png", confidence=.8))
        pydirectinput.click(ready_button_cords.x, ready_button_cords.y)
    except:
        print("Error in finding fill and or ready button and loading into game.")


def go_to_lobby(resolution):
    # DEPENDING ON THE RESOLUTION, THE EXACT ORDER OF CLICKS AND BUTTON INPUTS IS MAPPED OUT
    if resolution == "HD":
        pydirectinput.click(1628, 1050)
        sleep(1)
        pydirectinput.click(850, 716)
        sleep(7)
        pydirectinput.click(850, 716)
        pydirectinput.press("space")
        sleep(2)
        pydirectinput.press("space")
        sleep(1)
        pydirectinput.press("space")
        sleep(1)
        pydirectinput.press("space")
    else:
        pydirectinput.click(2171, 1400)
        sleep(1)
        pydirectinput.click(1131, 955)
        sleep(7)
        pydirectinput.click(1231, 955)
        pydirectinput.press("space")
        sleep(2)
        pydirectinput.press("space")
        sleep(1)
        pydirectinput.press("space")
        sleep(1)
        pydirectinput.press("space")


class ApexBot:
    def __init__(self, resolution):
        self.in_game = False
        self.resolution = resolution

    def xp_grinding(self):
        # CHECKS TO SEE IF APEX IS STILL OPEN, IF IT IS THEN IT CHECKS FOR CERTAIN BUTTONS OR ICONS ON THE SCREEN TO DETERMINE ITS NEXT ACTION
        if "r5apex.exe" not in [p.name() for p in process_iter()]:
            pass
        elif pyautogui.locateOnScreen(f"in_game_constant{self.resolution}.png", confidence=.8) is not None:
            self.in_game = True
            print("Jump")
            pydirectinput.press("space")
            sleep(randint(0, 10))
        elif pyautogui.locateOnScreen(f"ready_button{self.resolution}.png", confidence=.8) is not None:
            print("Start")
            queue_into_game(self.resolution)
            self.in_game = False
        elif pyautogui.locateOnScreen(f"squad_eliminated_constant{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"leave_match_constant{self.resolution}.png", confidence=.8) is not None:
            print("End")
            go_to_lobby(self.resolution)
            self.in_game = False
        elif pyautogui.locateOnScreen(f"continue_constant{self.resolution}.png", confidence=.8) is not None:
            print("Clicking game")
            pydirectinput.click()
            self.in_game = False
        elif pyautogui.locateOnScreen(f"escape_close{self.resolution}.png", confidence=.8) is not None:
            print("Pressing Escape")
            pydirectinput.press("escape")
            self.in_game = False
        elif pyautogui.locateOnScreen(f"continue_error{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"continue_error2_{self.resolution}.png", confidence=.8):
            print("Pressing Continue")
            pydirectinput.press("escape")
            self.in_game = False
        else:
            print("Not in game")
            self.in_game = False

    def kd_lowering(self, interact_key, tactical_key):
        # CHECKS TO SEE IF APEX IS STILL OPEN, IF IT IS THEN IT CHECKS FOR CERTAIN BUTTONS OR ICONS ON THE SCREEN TO DETERMINE ITS NEXT ACTION
        if "r5apex.exe" not in [p.name() for p in process_iter()]:
            pass
        elif pyautogui.locateOnScreen(f"in_game_constant{self.resolution}.png", confidence=.8) is not None:
            self.in_game = True
            print("Jump")
            pydirectinput.press("space")
            sleep(randint(0, 10))
            pydirectinput.press(tactical_key)
        elif pyautogui.locateOnScreen(f"ready_button{self.resolution}.png", confidence=.8) is not None:
            print("Start")
            queue_into_game(self.resolution)
            self.in_game = False
        elif pyautogui.locateOnScreen(f"horizon{self.resolution}.png", confidence=.8) is not None:
            print("Selecting Horizon")
            # SELECTS HORIZON AND IF HORIZON CAN'T BE SELECTED IT PREVENTS THE PROGRAM FROM CRASHING
            try:
                button_cords = pyautogui.center(pyautogui.locateOnScreen(f"horizon{self.resolution}.png", confidence=.8))
                pydirectinput.click(button_cords.x, button_cords.y)
            except:
                print("Horizon cords were not found")
        elif pyautogui.locateOnScreen(f"gibraltar{self.resolution}.png", confidence=.8) is not None:
            print("Selecting Gibraltar")
            # SELECTS HORIZON AND IF GIBRALTAR CAN'T BE SELECTED IT PREVENTS THE PROGRAM FROM CRASHING
            try:
                button_cords = pyautogui.center(pyautogui.locateOnScreen(f"gibraltar{self.resolution}.png", confidence=.8))
                pydirectinput.click(button_cords.x, button_cords.y)
            except:
                print("Gibraltar cords were not found")
        elif pyautogui.locateOnScreen(f"launch{self.resolution}.png", confidence=.7) is not None:
            sleep(3)
            print("Launch")
            pydirectinput.press(interact_key)
            pydirectinput.moveTo(990, 985, 0.5)
            pydirectinput.keyDown("w")
            sleep(15)
            pydirectinput.keyUp("w")
        elif pyautogui.locateOnScreen(f"squad_eliminated_constant{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"leave_match_constant{self.resolution}.png", confidence=.8) is not None:
            print("End")
            go_to_lobby(self.resolution)
            self.in_game = False
        elif pyautogui.locateOnScreen(f"continue_constant{self.resolution}.png", confidence=.8) is not None:
            print("Clicking game")
            pydirectinput.click()
            self.in_game = False
        elif pyautogui.locateOnScreen(f"escape_close{self.resolution}.png", confidence=.8) is not None:
            print("Pressing Escape")
            pydirectinput.press("escape")
            self.in_game = False
        elif pyautogui.locateOnScreen(f"continue_error{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"continue_error2_{self.resolution}.png", confidence=.8):
            print("Pressing Continue")
            pydirectinput.press("escape")
            self.in_game = False
        else:
            print("Not in game")
            self.in_game = False
