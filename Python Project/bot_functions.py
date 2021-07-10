import pyautogui
import pydirectinput
from time import sleep
from random import randint
from psutil import process_iter


def queue_into_game(resolution):
    if resolution == "HD":
        fill_button_cords = pyautogui.center(pyautogui.locateOnScreen("fill_teammatesHD.png"))
        pydirectinput.click(fill_button_cords.x, fill_button_cords.y)
        sleep(1)
        pydirectinput.click(130, 953)
    else:
        fill_button_cords = pyautogui.center(pyautogui.locateOnScreen("fill_teammates2K.png"))
        pydirectinput.click(fill_button_cords.x, fill_button_cords.y)
        sleep(1)
        pydirectinput.click(174, 1271)


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


class ApexBot:
    def __init__(self, resolution):
        self.in_game = False
        self.resolution = resolution

    def xp_grinding(self):
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
        elif pyautogui.locateOnScreen(f"disconnected_player_constant{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"error_constant{self.resolution}.png", confidence=.8):
            print("Reconnecting")
            if self.resolution == "HD":
                pydirectinput.click(957, 722)
            else:
                pydirectinput.click(1275, 963)
            self.in_game = False
        else:
            print("Not in game")
            self.in_game = False

    def kd_lowering(self, interact_key, tactical_key):
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
            if self.resolution == "HD":
                pydirectinput.click(1420, 588)
            else:
                pydirectinput.click(1892, 784)
        elif pyautogui.locateOnScreen(f"gibraltar{self.resolution}.png", confidence=.8) is not None:
            print("Selecting Gibraltar")
            if self.resolution == "HD":
                pydirectinput.click(1250, 440)
            else:
                pydirectinput.click(1665, 455)
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
        elif pyautogui.locateOnScreen(f"disconnected_player_constant{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"error_constant{self.resolution}.png", confidence=.8):
            print("Reconnecting")
            if self.resolution == "HD":
                pydirectinput.click(957, 722)
            else:
                pydirectinput.click(1275, 963)
            self.in_game = False
        else:
            print("Not in game")
            self.in_game = False
