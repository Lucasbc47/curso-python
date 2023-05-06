import pyautogui

# Obtém uma lista de objetos "Window" correspondente a todas as janelas abertas
window_list = pyautogui.getAllWindows()

# Extrai o título de cada janela e imprime na tela
for window in window_list:
    print(window.title)
    

""""
pyautogui.dragTo(100, 200, button='left')     # drag mouse to X of 100, Y of 200 while holding down left mouse button
>>> pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
>>> pyautogui.drag(30, 0, 2, button='right')   # drag the mouse left 30 pixels over 2 seconds while holding down the right mouse button
"""             