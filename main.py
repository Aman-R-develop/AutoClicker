import mouse
import keyboard
import time
while True:
    if keyboard.is_pressed('/') == True:
        mouse.press()
        mouse.release()
        mouse.press()
        mouse.release()
        time.sleep(0.05)
    else:
        pass
