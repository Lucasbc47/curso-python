import pyautogui
import time

from tkinter import filedialog


pyautogui.alert("O código vai começar, não mexa no computador enquanto o código está rodandando, não esqueça de preencher o caminho do arquivo antes de iniciar e ler os comentários no código e feche a janela do chrome.", "Atencao")


file_path = filedialog.askopenfilename()

def fix(text: str) -> str:
    new = text.replace("/", "\\")
    return new

email = pyautogui.prompt("Insira seu email:")
password = pyautogui.password("Insira sua senha:")

pyautogui.PAUSE = 0.5

with pyautogui.hold("win"):
    pyautogui.press("r")

pyautogui.write("chrome -incognito")    
pyautogui.press("enter")
time.sleep(0.8)
pyautogui.write("http://drive.google.com/")

# Se a janela do chrome não estiver maximizada e tiver erros, descomente essas 2 linhas de código:
# pyautogui.hotkey("win", "up")
# pyautogui.hotkey("win", "up")

pyautogui.press("enter")
time.sleep(3)

for i in range(0, 9):
    pyautogui.press("tab")

pyautogui.press("enter")
time.sleep(3)


pyautogui.write(email)
pyautogui.press("enter")
time.sleep(4)
pyautogui.write(password)       
pyautogui.press("enter")

time.sleep(5)
pyautogui.hotkey("shift", "u")
pyautogui.write(fix(file_path))
pyautogui.press("enter")




