import pyautogui
import time

remetente = pyautogui.prompt("Insira email do remetente:")
titulo = pyautogui.prompt("Insira titulo do email:")
desc = pyautogui.prompt("Insira o corpo do email:")
email = pyautogui.prompt("Insira seu email:")
password = pyautogui.password("Insira sua senha:")

pyautogui.PAUSE = 0.5

with pyautogui.hold("win"):     
    pyautogui.press("r")

pyautogui.write("chrome -incognito")    
pyautogui.press("enter")            

time.sleep(0.8)

pyautogui.write("https://gmail.com")
pyautogui.press("enter")
time.sleep(5)
pyautogui.write(email)
time.sleep(3)
pyautogui.press("enter")
time.sleep(5)
pyautogui.write(password)       
pyautogui.press("enter")

# time.sleep(3)

time.sleep(5)

for i in range(0, 15):
    pyautogui.press("tab")

pyautogui.press("enter")
time.sleep(0.5)

pyautogui.write(remetente)
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.write(titulo)
pyautogui.press("tab")
pyautogui.write(desc)
pyautogui.press("tab")
pyautogui.press("enter")