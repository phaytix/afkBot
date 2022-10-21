import pyautogui as pag
import random
import time

while True:
    # Monitor Coordinates
    x = random.randint(600,700)
    y = random.randint(200,600)
    
    # Mouse speed
    pag.moveTo(x,y,0.5)

    # Time till mouse moves
    time.sleep(2)
