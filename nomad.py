import time
import pyautogui

def handle_popups():
        popup_found = False
        check = False
        imgs = ["./imgs/close/cross1.png","./imgs/close/cross2.png","./imgs/close/cross3.png","./imgs/close/cross4.png","./imgs/close/tick1.png","./imgs/close/tick2.png"]
        for img_address in imgs:
                find = pyautogui.locateOnScreen(img_address,confidence = 0.8)
                if(find):
                        popup_found = True
                        check = True
                        pyautogui.moveTo(find)
                        pyautogui.click()
                        time.sleep(0.2)
        while(check):
                check = False
                for img_address in imgs:
                        find = pyautogui.locateOnScreen(img_address,confidence = 0.8)
                        if(find):
                                check = True
                                pyautogui.moveTo(find)
                                pyautogui.click()
                                time.sleep(0.5)
        return popup_found


print("how many (1hr skips) divided by 4 u wanna use?")
val = int(input())
print("you are going to use ", val*4 ," 1hr skips")

camps = [("541","697"),("541","695"),("537","695"),("542","696")]
for i in range(val):
    j=0
    while(j<4):
        skip = "hour"
        repeat = False
        x_cord,y_cord = camps[j][0],camps[j][1]
        pyautogui.doubleClick(x=823,y=90)
        pyautogui.write(x_cord)
        pyautogui.doubleClick(x=876, y=92)
        pyautogui.write(y_cord)
        pyautogui.click(x=942, y=107)
        time.sleep(1)
        pyautogui.click(x=1072, y=591)#attack option
        time.sleep(1)
        skip_time = pyautogui.locateOnScreen("./imgs/nomad/skip_time.png",confidence = 0.9)
        if(skip_time):
            pyautogui.moveTo(skip_time)
            pyautogui.click()
            time.sleep(1)
            if(skip == "hour"):
                hr_skip = pyautogui.locateOnScreen("./imgs/nomad/1hr_skip.png",confidence = 0.9)
                if(hr_skip):
                    pyautogui.moveTo(hr_skip)
                    x,y = pyautogui.position()
                    x+=100
                    pyautogui.moveTo(x=x,y=y)
                    pyautogui.click()
        time.sleep(1.5)
        ok_attack = pyautogui.locateOnScreen("./imgs/ok.png",confidence = 0.9)
        if(ok_attack):
            pyautogui.moveTo(ok_attack)
            pyautogui.click()
            time.sleep(3) #attack screen appears
            pyautogui.click(x=554, y=922)#present drop down
            time.sleep(2)
            pyautogui.click(x=513, y=899)#select present
            pyautogui.click(x=763, y=924)#apply to all
            clear_curr_wave = pyautogui.locateOnScreen("./imgs/nomad/clear_curr_wave.png",confidence = 0.9)
            if(clear_curr_wave):
                pyautogui.moveTo(clear_curr_wave)
                pyautogui.click()
                pyautogui.click(x=554, y=922)#present drop down
                time.sleep(2)
                pyautogui.click(x=529, y=881)#select present
                #time.sleep(60*10)
                apply_curr_wave = pyautogui.locateOnScreen("./imgs/nomad/apply_curr_wave.png",confidence = 0.9)
                if(apply_curr_wave):
                    pyautogui.moveTo(apply_curr_wave)
                    pyautogui.click()
                    attack = pyautogui.locateOnScreen("./imgs/attack.png",confidence = 0.9)
                    if(attack):
                        pyautogui.moveTo(attack)
                        pyautogui.click()
                        pyautogui.click(x=689, y=543)#coin-horses
                        pyautogui.click(x=1130, y=813)#click ok
                        time.sleep(1.5)
        popup = handle_popups()
        if(popup):
            continue
        else:
            j+=1
    time.sleep(3*60 - 20)
    handle_popups()
        
                
            
    
        
            
            
                    


