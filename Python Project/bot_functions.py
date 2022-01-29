import pyautogui
import pydirectinput
from time import sleep
from random import randint
from psutil import process_iter


# QUEUES FOR A MATCH FROM THE HOME SCREEN
def queue_into_game(resolution):
    try:
        if pyautogui.locateOnScreen(f"fill_teammates{resolution}.png", confidence=.95) is not None:
            fill_button_cords = pyautogui.center(pyautogui.locateOnScreen(f"fill_teammates{resolution}.png", confidence=.8))
            pydirectinput.click(fill_button_cords.x, fill_button_cords.y)
        sleep(1)
        ready_button_cords = pyautogui.center(pyautogui.locateOnScreen(f"ready_button{resolution}.png", confidence=.8))
        pydirectinput.click(ready_button_cords.x, ready_button_cords.y)
    except:
        print("Error in finding fill and or ready button and loading into game.")


# ENTERS CLICKS AND KEYSTROKES IN CORRECT ORDER TO GO FROM THE DEATH SCREEN TO THE LOBBY
def go_to_lobby(resolution):
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
        sleep(1)
        pydirectinput.press("space")


class ApexBot:
    def __init__(self, resolution):
        self.in_game = False
        self.resolution = resolution

    def xp_grinding(self):
        # CHECKS IF APEX IS CURRENTLY RUNNING
        if "r5apex.exe" not in [p.name() for p in process_iter()]:
            pass
        # STOPS PLAYER FROM BEING KICKED FOR AFKING BY JUMPING
        elif pyautogui.locateOnScreen(f"in_game_constant{self.resolution}.png", confidence=.8) is not None:
            self.in_game = True
            pydirectinput.press("space")
            sleep(randint(0, 10))
        # STARTS QUEUING
        elif pyautogui.locateOnScreen(f"ready_button{self.resolution}.png", confidence=.8) is not None:
            queue_into_game(self.resolution)
            self.in_game = False
        # GOES FROM DEATH SCREEN TO HOME SCREEN
        elif pyautogui.locateOnScreen(f"squad_eliminated_constant{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"leave_match_constant{self.resolution}.png", confidence=.8) is not None:
            go_to_lobby(self.resolution)
            self.in_game = False
        # CLICKS THE CONTINUE BUTTON THAT APPEARS WHEN APEX IS FIRST LAUNCHED
        elif pyautogui.locateOnScreen(f"continue_constant{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.click()
            self.in_game = False
        # PRESSES ESCAPE WHEN A POPUP IS ON SCREEN
        elif pyautogui.locateOnScreen(f"escape_close{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.press("escape")
            self.in_game = False
        # GETS USER BACK INTO THE GAME WHEN AN ERROR HAPPENS E.G. BEING DISCONNECTED
        elif pyautogui.locateOnScreen(f"continue_error{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"continue_error2_{self.resolution}.png", confidence=.8):
            pydirectinput.press("escape")
            self.in_game = False
        else:
            self.in_game = False

    def kd_lowering(self, interact_key, tactical_key):
        # CHECKS IF APEX IS CURRENTLY RUNNING
        if "r5apex.exe" not in [p.name() for p in process_iter()]:
            pass
        # STOPS PLAYER FROM BEING KICKED FOR AFKING BY JUMPING AND USES THEIR TACTICAL TO MAKE THEM MORE VISIBLE
        elif pyautogui.locateOnScreen(f"in_game_constant{self.resolution}.png", confidence=.8) is not None:
            self.in_game = True
            pydirectinput.press("space")
            sleep(randint(0, 10))
            pydirectinput.press(tactical_key)
        # STARTS QUEUING
        elif pyautogui.locateOnScreen(f"ready_button{self.resolution}.png", confidence=.8) is not None:
            print("Start")
            queue_into_game(self.resolution)
            self.in_game = False
        # TRIES TO SELECT HORIZON, THEN GIBBY
        elif self.in_game is False and pyautogui.locateOnScreen(f"horizon{self.resolution}.png", confidence=.8) is not None:
            try:
                button_cords = pyautogui.center(pyautogui.locateOnScreen(f"horizon{self.resolution}.png", confidence=.8))
                pydirectinput.click(button_cords.x, button_cords.y)
            except:
                print("Horizon cords were not found")
                if pyautogui.locateOnScreen(f"gibraltar{self.resolution}.png", confidence=.8) is not None:
                    try:
                        button_cords = pyautogui.center(pyautogui.locateOnScreen(f"gibraltar{self.resolution}.png", confidence=.8))
                        pydirectinput.click(button_cords.x, button_cords.y)
                    except:
                        print("Gibraltar cords were not found")
        # DROPS THE USER FROM THE LAUNCH SHIP IN AN AREA USUALLY DENSE WITH PLAYERS
        elif pyautogui.locateOnScreen(f"launch{self.resolution}.png", confidence=.7) is not None:
            sleep(3)
            pydirectinput.press(interact_key)
            pydirectinput.moveTo(990, 985, 0.5)
            pydirectinput.keyDown("w")
            sleep(15)
            pydirectinput.keyUp("w")
        # GOES FROM DEATH SCREEN TO HOME SCREEN
        elif pyautogui.locateOnScreen(f"squad_eliminated_constant{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"leave_match_constant{self.resolution}.png", confidence=.8) is not None:
            go_to_lobby(self.resolution)
            self.in_game = False
        # CLICKS THE CONTINUE BUTTON THAT APPEARS WHEN APEX IS FIRST LAUNCHED
        elif pyautogui.locateOnScreen(f"continue_constant{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.click()
            self.in_game = False
        # PRESSES ESCAPE WHEN A POPUP IS ON SCREEN
        elif pyautogui.locateOnScreen(f"escape_close{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.press("escape")
            self.in_game = False
        # GETS USER BACK INTO THE GAME WHEN AN ERROR HAPPENS E.G. BEING DISCONNECTED
        elif pyautogui.locateOnScreen(f"continue_error{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"continue_error2_{self.resolution}.png", confidence=.8):
            pydirectinput.press("escape")
            self.in_game = False
        else:
            self.in_game = False
