import pyautogui
import time

time.sleep(1)
pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("clickspeedtest.com")
time.sleep(1)
pyautogui.press("Enter")
time.sleep(1)
pyautogui.moveTo(770,681)
time.sleep(1)
for i in range (0,47):
    pyautogui.tripleClick()
