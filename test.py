import pyautogui
import time
def handle_popups():
        popup_found = False
        check = False
        imgs = ["./imgs/close/cross1.png","./imgs/close/cross2.png","./imgs/close/cross3.png","./imgs/close/cross4.png","./imgs/close/tick1.png","./imgs/close/tick2.png"]
        for img_address in imgs:
                find = pyautogui.locateOnScreen(img_address,confidence = 0.5)
                if(find):
                        popup_found = True
                        check = True
                        pyautogui.moveTo(find)
                        pyautogui.click()
                        time.sleep(0.2)
        while(check):
                check = False
                for img_address in imgs:
                        find = pyautogui.locateOnScreen(img_address,confidence = 0.5)
                        if(find):
                                check = True
                                pyautogui.moveTo(find)
                                pyautogui.click()
                                time.sleep(0.5)
        return popup_found

#found = pyautogui.locateOnScreen("./imgs/kingdoms/farstar.png",confidence = 0.9)
#found = pyautogui.locateOnScreen("./imgs/kingdoms/gathalamor.png",confidence = 0.9)
#found = pyautogui.locateOnScreen("./imgs/kingdoms/hesperus.png",confidence = 0.9)
#found = pyautogui.locateOnScreen("./imgs/kingdoms/gathalamor.png",confidence = 0.8)

pyautogui.click(x=1819, y=817)
#if found:
#        pyautogui.moveTo(found)
#print(found)
#handle_popups()
#pyautogui.click(x=1831, y=949)
