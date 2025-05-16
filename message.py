import pyautogui, time
time.sleep(4)
count = 0
while count<50:
    pyautogui.typewrite("Hello", interval=0.02)
    pyautogui.press("Enter")
    count = count+1