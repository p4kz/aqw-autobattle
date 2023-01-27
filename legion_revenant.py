import pyautogui
import time

def legion_revenant (amount):
      pyautogui.click(200, 200) # Auto-target game window top left
  
      for i in range(1, amount):
        pyautogui.typewrite('2')
        time.sleep(3)
        pyautogui.typewrite('3')
        time.sleep(3)

# Replace AMOUNT with the amount of monsters you want killed
legion_revenant (AMOUNT)