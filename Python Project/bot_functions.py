import pyautogui
import pydirectinput
from time import sleep
from random import randint
from psutil import process_iter


class ApexBot:
    def __init__(self, resolution):
        self.in_game = False
        self.resolution = resolution
        self.tries_to_find_fill_button = 0

    def xp_rotation(self):
        # CHECKS IF APEX IS CURRENTLY RUNNING
        if "r5apex.exe" not in [p.name() for p in process_iter()]:
            pass     
        # STOPS PLAYER FROM BEING KICKED FOR AFKING BY JUMPING   
        elif pyautogui.locateOnScreen(f"Game Assets/in_game_constant{self.resolution}.png", confidence=.8) is not None:
            self.in_game = True
            pydirectinput.press("space")
            sleep(randint(0, 10))
        # CLICKS THE CONTINUE BUTTON THAT APPEARS WHEN APEX IS FIRST LAUNCHED
        elif pyautogui.locateOnScreen(f"Game Assets/continue_constant{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.click()
            self.in_game = False
        # STARTS QUEUING
        elif pyautogui.locateOnScreen(f"Game Assets/ready_button{self.resolution}.png", confidence=.8) is not None:
            self.queue_into_game()
            self.in_game = False
        # GOES FROM DEATH SCREEN TO HOME SCREEN
        elif pyautogui.locateOnScreen(f"Game Assets/squad_eliminated_constant{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"Game Assets/leave_match_constant{self.resolution}.png", confidence=.8) is not None:
            self.to_lobby_rotation()
            self.in_game = False
        # PRESSES ESCAPE WHEN A POPUP IS ON SCREEN
        elif pyautogui.locateOnScreen(f"Game Assets/escape{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.press("escape")
            self.in_game = False
        # GETS USER BACK INTO THE GAME WHEN AN ERROR HAPPENS E.G. BEING DISCONNECTED
        elif pyautogui.locateOnScreen(f"Game Assets/continue_error{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"Game Assets/continue_error2_{self.resolution}.png", confidence=.8):
            pydirectinput.press("escape")
            self.in_game = False
        else:
            self.in_game = False

    def xp_grinding(self):
        # CHECKS IF APEX IS CURRENTLY RUNNING
        if "r5apex.exe" not in [p.name() for p in process_iter()]:
            pass     
        # STOPS PLAYER FROM BEING KICKED FOR AFKING BY JUMPING   
        elif pyautogui.locateOnScreen(f"Game Assets/in_game_constant{self.resolution}.png", confidence=.8) is not None:
            self.in_game = True
            pydirectinput.press("space")
            sleep(randint(0, 10))
        # CLICKS THE CONTINUE BUTTON THAT APPEARS WHEN APEX IS FIRST LAUNCHED
        elif pyautogui.locateOnScreen(f"Game Assets/continue_constant{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.click()
            self.in_game = False
        # STARTS QUEUING
        elif pyautogui.locateOnScreen(f"Game Assets/ready_button{self.resolution}.png", confidence=.8) is not None:
            self.queue_into_game()
            self.in_game = False
        # GOES FROM DEATH SCREEN TO HOME SCREEN
        elif pyautogui.locateOnScreen(f"Game Assets/scoreboard.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"Game Assets/scoreboard.png", confidence=.8) is not None:
            self.go_to_lobby()
            self.in_game = False 
        # PRESSES ESCAPE WHEN A POPUP IS ON SCREEN
        elif pyautogui.locateOnScreen(f"Game Assets/escape{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.press("escape")
            self.in_game = False
        # GETS USER BACK INTO THE GAME WHEN AN ERROR HAPPENS E.G. BEING DISCONNECTED
        elif pyautogui.locateOnScreen(f"Game Assets/continue_error{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"Game Assets/continue_error2_{self.resolution}.png", confidence=.8):
            pydirectinput.press("escape")
            self.in_game = False
        else:
            self.in_game = False

    def kd_lowering(self, interact_key, tactical_key):
        # CHECKS IF APEX IS CURRENTLY RUNNING
        if "r5apex.exe" not in [p.name() for p in process_iter()]:
            pass
        # STOPS PLAYER FROM BEING KICKED FOR AFKING BY JUMPING AND USES THEIR TACTICAL TO MAKE THEM MORE VISIBLE
        elif pyautogui.locateOnScreen(f"Game Assets/in_game_constant{self.resolution}.png", confidence=.8) is not None:
            self.in_game = True
            pydirectinput.press("space")
            sleep(randint(0, 10))
            pydirectinput.press(tactical_key)
        # STARTS QUEUING
        elif pyautogui.locateOnScreen(f"Game Assets/ready_button{self.resolution}.png", confidence=.8) is not None:
            self.queue_into_game()
            self.in_game = False
        # TRIES TO SELECT HORIZON, THEN GIBBY
        elif pyautogui.locateOnScreen(f"Game Assets/horizon{self.resolution}.png", confidence=.7) is not None:
            try:
                button_cords = pyautogui.center(pyautogui.locateOnScreen(f"Game Assets/horizon{self.resolution}.png", confidence=.8))
                pydirectinput.click(button_cords.x, button_cords.y)
            except:
                print("Horizon cords were not found")
                if pyautogui.locateOnScreen(f"Game Assets/gibraltar{self.resolution}.png", confidence=.7) is not None:
                    try:
                        button_cords = pyautogui.center(pyautogui.locateOnScreen(f"Game Assets/gibraltar{self.resolution}.png", confidence=.8))
                        pydirectinput.click(button_cords.x, button_cords.y)
                    except:
                        print("Gibraltar cords were not found")
        # DROPS THE USER FROM THE LAUNCH SHIP IN AN AREA USUALLY DENSE WITH PLAYERS
        elif pyautogui.locateOnScreen(f"Game Assets/launch{self.resolution}.png", confidence=.7) is not None:
            sleep(3)
            pydirectinput.press(interact_key)
            pydirectinput.moveTo(990, 985, 0.5)
            pydirectinput.keyDown("w")
            sleep(15)
            pydirectinput.keyUp("w")
        # GOES FROM DEATH SCREEN TO HOME SCREEN
        elif pyautogui.locateOnScreen(f"Game Assets/squad_eliminated_constant{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"Game Assets/leave_match_constant{self.resolution}.png", confidence=.8) is not None:
            self.go_to_lobby()
            self.in_game = False
        # CLICKS THE CONTINUE BUTTON THAT APPEARS WHEN APEX IS FIRST LAUNCHED
        elif pyautogui.locateOnScreen(f"Game Assets/continue_constant{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.click()
            self.in_game = False
        # PRESSES ESCAPE WHEN A POPUP IS ON SCREEN
        elif pyautogui.locateOnScreen(f"Game Assets/escape{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.press("escape")
            self.in_game = False
        # GETS USER BACK INTO THE GAME WHEN AN ERROR HAPPENS E.G. BEING DISCONNECTED
        elif pyautogui.locateOnScreen(f"Game Assets/continue_error{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"Game Assets/continue_error2_{self.resolution}.png", confidence=.8):
            pydirectinput.press("escape")
            self.in_game = False
        else:
            self.in_game = False

    # QUEUES FOR A MATCH FROM THE HOME SCREEN
    def queue_into_game(self):
        try:
            print("Trying to queue into game")
            if pyautogui.locateOnScreen(f"Game Assets/fill_teammates{self.resolution}.png", confidence=.6) is not None:
                self.tries_to_find_fill_button = 0
                fill_button_cords = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/fill_teammates{self.resolution}.png", confidence=.6))
                pydirectinput.click(fill_button_cords.x, fill_button_cords.y)
                sleep(1)
                ready_button_cords = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/ready_button{self.resolution}.png", confidence=.8))
                pydirectinput.click(ready_button_cords.x, ready_button_cords.y)
                sleep(20)
                #SPAWNS INTO MATCH IN CASE OF CONTROL MODE
                #ICON1
                spawn_button_cords1 = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/spawn1.png", confidence=.6))
                pydirectinput.click(spawn_button_cords1.x, ready_button_cord1s.y)
                #ICON2
                spawn_button_cords2 = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/spawn2.png", confidence=.6))
                pydirectinput.click(spawn_button_cords2.x, ready_button_cord2s.y)
                #ICON3
                spawn_button_cords3 = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/spawn3.png", confidence=.6))
                pydirectinput.click(spawn_button_cords3.x, ready_button_cords3.y)

            else:
                self.tries_to_find_fill_button += 1
                sleep(1)

            if self.tries_to_find_fill_button >= 5:
                self.tries_to_find_fill_button = 0
                ready_button_cords = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/ready_button{self.resolution}.png", confidence=.8))
                pydirectinput.click(ready_button_cords.x, ready_button_cords.y)
        except:
            print("Error in finding fill and or ready button and loading into game.")

    # ENTERS CLICKS AND KEYSTROKES IN CORRECT ORDER TO GO FROM THE DEATH SCREEN TO THE LOBBY
    def go_to_lobby(self):
        if self.resolution == "HD":
            pydirectinput.press("space")
            sleep(1)
            if pyautogui.locateOnScreen(f"Game Assets/yes_button{self.resolution}.png", confidence=.8) is not None:
                yes_button_cords = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/yes_button{self.resolution}.png", confidence=.8))
                pydirectinput.click(yes_button_cords.x, yes_button_cords.y)
            elif pyautogui.locateOnScreen(f"Game Assets/yes_button2_{self.resolution}.png", confidence=.8) is not None:
                yes_button_cords = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/yes_button2_{self.resolution}.png", confidence=.8))
                pydirectinput.click(yes_button_cords.x, yes_button_cords.y)
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
            pydirectinput.press("space")
            sleep(1)
            if pyautogui.locateOnScreen(f"Game Assets/yes_button{self.resolution}.png", confidence=.8) is not None:
                yes_button_cords = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/yes_button{self.resolution}.png", confidence=.8))
                pydirectinput.click(yes_button_cords.x, yes_button_cords.y)
            elif pyautogui.locateOnScreen(f"Game Assets/yes_button2_{self.resolution}.png", confidence=.8) is not None:
                yes_button_cords = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/yes_button2_{self.resolution}.png", confidence=.8))
                pydirectinput.click(yes_button_cords.x, yes_button_cords.y)
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

    # ENTERS CLICKS AND KEYSTROKES IN CORRECT ORDER TO GO FROM THE DEATH SCREEN TO THE LOBBY in random modes.
    def to_lobby_rotation(self):
        print("Entered lobby modes function")
        pydirectinput.press("space")
        sleep(1)
        if pyautogui.locateOnScreen(f"Game Assets/esc_menu{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.press("escape")
            print("found the escape")

        if pyautogui.locateOnScreen(f"Game Assets/leave_match_constant{self.resolution}.png", confidence=.8) is not None:
            print("found the leave match button")
            #PRESSES THE LEAVE BUTTON
            leave_button_cords = pyautogui.center(
                pyautogui.locateOnScreen(f"Game Assets/leave_match_constant{self.resolution}.png", confidence=.8))
            pydirectinput.click(leave_button_cords.x, leave_button_cords.y)
            #PRESSES THE YES BUTTON
            yess_button_cords = pyautogui.center(
                pyautogui.locateOnScreen(f"Game Assets/yes_button{self.resolution}.png", confidence=.8))
            pydirectinput.click(yess_button_cords.x, yess_button_cords.y)
        #GOES FOR THE SPACE 
        sleep(9)
        pydirectinput.press("space")
        sleep(2)
        pydirectinput.press("space")
        sleep(2)
        pydirectinput.press("space")
        sleep(1)
        pydirectinput.press("space")
