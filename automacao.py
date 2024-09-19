import pyautogui
import time

pyautogui.PAUSE = 0.3 # Função para esperar 3 segundos a cada execução do pyautogui

# pegar posições do mouse e da tela
print(pyautogui.position()) # a posição a onde estar o mouse
print(pyautogui.size()) # tamanho da resolução da tela 

# clicar com o mouse
time.sleep(3)
pyautogui.moveTo(x=704, y=881, duration=1)
time.sleep(2)
pyautogui.click(x=704, y=881)

time.sleep(4)
pyautogui.moveTo(x=156, y=16, duration=1) # função para fazer o mouse clicar na posição que tiver. 
time.sleep(2)
pyautogui.click(x=156, y=16)

time.sleep(3)
pyautogui.moveTo(x=593, y=191, duration=1)
time.sleep(2)
pyautogui.click(x=593, y=191)

time.sleep(3)
pyautogui.moveTo(x=649, y=651, duration=1)
time.sleep(2)
pyautogui.click(x=649, y=651)

time.sleep(3)
pyautogui.scroll(-600)