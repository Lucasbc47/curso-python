from tkinter import filedialog

import pyautogui
import time


class LUAC:
    def __init__(self):
        self.email = pyautogui.prompt("Insira seu email")
        self.password = pyautogui.password("Insira sua senha")

        with pyautogui.hold("win"):
            pyautogui.press("r")
        pyautogui.write("chrome -incognito")
        pyautogui.press("enter")
        time.sleep(0.8)


    def fix(self, text: str) -> str:
        new = text.replace("/", "\\")
        return new



    def send_email(self):
        self.destinario = pyautogui.prompt("Insira o email do destinário")
        self.title = pyautogui.prompt("Insira titulo do email")
        self.body = pyautogui.prompt("Insira o corpo do email")
        
        pyautogui.write("https://gmail.com")
        pyautogui.press("enter")
        time.sleep(5)
        pyautogui.write(self.email)
        time.sleep(3)
        pyautogui.press("enter")
        time.sleep(5)
        pyautogui.write(self.password)       
        pyautogui.press("enter")
        time.sleep(5)

        for i in range(0, 15):
            pyautogui.press("tab")

        pyautogui.press("enter")
        time.sleep(0.5)

        pyautogui.write(self.destinario)
        pyautogui.press("enter")
        pyautogui.press("tab")
        pyautogui.write(self.title)
        pyautogui.press("tab")
        pyautogui.write(self.body)
        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.hotkey("alt", "f4")
        pyautogui.press("enter")


    def upload_file_gdrive(self):
        self.file_location = self.fix(filedialog.askopenfilename())

        pyautogui.write("http://drive.google.com/")
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.write(self.email)
        pyautogui.press("enter")
        pyautogui.write(self.password)       
        pyautogui.press("enter")
        
        time.sleep(5)

        for i in range(0, 9):
            pyautogui.press("tab")

        pyautogui.press("enter")
        time.sleep(3)


        pyautogui.write(self.email)
        pyautogui.press("enter")
        time.sleep(4)
        pyautogui.write(self.password)       
        pyautogui.press("enter")

        time.sleep(5)
        pyautogui.hotkey("shift", "u")
        pyautogui.write(self.file_location)
        pyautogui.press("enter")
        pyautogui.hotkey("alt", "f4")

        