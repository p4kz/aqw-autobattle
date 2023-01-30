import PySimpleGUI as sg
import pyautogui
import re
import time

sg.theme('Default1')

layout = [  [sg.Text('Class: Legion Revenant         3s cooldown')],
            [sg.Text('Numero de kills'), sg.InputText(),],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('AUTO-BATTLE - p4kz', layout, size=(278,100))

def legion_revenant (amount):
      pyautogui.click(200, 200)
  
      for i in range(1, amount):
        pyautogui.typewrite('2')
        time.sleep(3)
        pyautogui.typewrite('3')
        time.sleep(3)
            
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    if re.search("[0-9]", values[0]):
        legion_revenant (int(values[0]))
    else: 
        print('error')
          
window.close()