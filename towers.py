import pyautogui
import time

#fire_towers = [('686', '563\n'), ('682', '565\n'), ('676', '564\n'), ('672', '565\n'), ('694', '562\n'), ('675', '560\n'), ('680', '559\n'), ('671', '559\n'), ('687', '559\n'), ('668', '564\n'), ('669', '553\n'), ('674', '554\n'), ('681', '554\n'), ('686', '555\n'), ('683', '550\n'), ('692', '557\n'), ('688', '550\n'), ('673', '571\n'), ('679', '568\n'), ('681', '572\n'), ('663', '565\n'), ('687', '570\n'), ('667', '568\n'), ('666', '573\n'), ('660', '568\n'), ('660', '562\n'), ('665', '560\n'), ('663', '552\n'), ('660', '555\n'), ('665', '548\n'), ('657', '558\n'), ('671', '548\n'), ('680', '547\n'), ('695', '553\n'), ('696', '558\n'), ('699', '555\n'), ('699', '562\n'), ('693', '568\n'), ('699', '568\n'), ('689', '577\n'), ('694', '573\n'), ('682', '576\n'), ('680', '581\n'), ('675', '578\n'), ('677', '574\n'), ('672', '575\n'), ('662', '572\n'), ('654', '568\n'), ('660', '568')]
#sand_towers = [('742', '577\n'), ('745', '571\n'), ('741', '570\n'), ('738', '580\n'), ('746', '580\n'), ('735', '574\n'), ('749', '577\n'), ('733', '578\n'), ('745', '584\n'), ('746', '566\n'), ('750', '581\n'), ('734', '582\n'), ('733', '569\n'), ('753', '574\n'), ('751', '568\n'), ('730', '573\n'), ('740', '587\n'), ('738', '563\n'), ('754', '579\n'), ('734', '565\n'), ('742', '562\n'), ('750', '586\n'), ('735', '587\n'), ('744', '589\n'), ('748', '562\n'), ('728', '579\n'), ('731', '585\n'), ('754', '584\n'), ('756', '569\n'), ('758', '573\n'), ('739', '559\n'), ('754', '564\n'), ('745', '558\n'), ('727', '566\n'), ('751', '590\n'), ('730', '562\n'), ('726', '583\n'), ('724', '575\n'), ('733', '559\n'), ('735', '592\n'), ('724', '569\n'), ('751', '558\n'), ('756', '589\n'), ('755', '560\n'), ('761', '581\n'), ('722', '581\n'), ('727', '590\n'), ('722', '588')]
#ice_towers = [('722', '609\n'), ('725', '612\n'), ('719', '613\n'), ('724', '617\n'), ('730', '611\n'), ('728', '606\n'), ('721', '604\n'), ('715', '612\n'), ('729', '617\n'), ('715', '607\n'), ('719', '621\n'), ('733', '615\n'), ('723', '600\n'), ('726', '622\n'), ('734', '607\n'), ('735', '611\n'), ('715', '620\n'), ('712', '616\n'), ('730', '621\n'), ('717', '600\n'), ('733', '603\n'), ('711', '605\n'), ('735', '619\n'), ('721', '596\n'), ('731', '598\n'), ('707', '610\n'), ('728', '595\n'), ('733', '626\n'), ('741', '608\n'), ('738', '599\n'), ('741', '619\n'), ('703', '612\n'), ('704', '604\n'), ('707', '598\n'), ('743', '604\n'), ('702', '608\n'), ('702', '619\n'), ('746', '610\n')]
#green_towers = [('548', '702\n'), ('542', '695\n'), ('545', '696\n'), ('549', '696\n'), ('539', '694\n'), ('536', '696\n'), ('535', '700\n'), ('533', '697\n'), ('533', '703\n'), ('532', '706\n'), ('535', '707\n'), ('538', '708\n'), ('541', '707\n'), ('546', '707\n'), ('549', '705\n'), ('553', '703\n'), ('552', '698\n'), ('555', '699\n'), ('546', '693\n'), ('543', '692\n'), ('540', '691\n'), ('536', '692\n'), ('529', '697\n'), ('530', '700\n'), ('529', '704\n'), ('528', '707\n'), ('536', '711\n'), ('540', '711\n'), ('544', '710\n'), ('549', '709\n'), ('552', '706\n'), ('556', '705\n'), ('542', '699\n'), ('542', '704\n'), ('538', '703\n'), ('539', '698\n'), ('545', '703\n'), ('547', '699')]

def hit_kingdom(kingdom):
        if(kingdom == "green"):
                time.sleep(2)
                x_p,y_p,file,done = select_kingdom("green")
                while(not done):
                        handle_popups()
                        x_p,y_p,file,done = select_kingdom("green")
                tower_round(x_p,y_p,file)

        if(kingdom == "fire"):
                time.sleep(1)
                handle_popups()
                x_p,y_p,file,done = select_kingdom("fire")
                while(not done):
                        handle_popups()
                        x_p,y_p,file,done = select_kingdom("fire")
                tower_round(x_p,y_p,file)

        if(kingdom == "sand"):
                time.sleep(1)
                handle_popups()
                x_p,y_p,file,done = select_kingdom("sand")
                while(not done):
                        handle_popups()
                        x_p,y_p,file,done = select_kingdom("sand")
                tower_round(x_p,y_p,file)

        if(kingdom == "ice"):
                time.sleep(1)
                handle_popups()
                x_p,y_p,file,done = select_kingdom("ice")
                while(not done):
                        handle_popups()
                        x_p,y_p,file,done = select_kingdom("ice")
                tower_round(x_p,y_p,file)

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
        
def select_kingdom(kingdom):
        done = False
        if(kingdom == "green"):
                x_p,y_p = 542,849
                #x_p,y_p = 558,901
                file = './towers/greentowers.txt'
                pyautogui.click(x=1826, y=939)
                time.sleep(0.5)
                pyautogui.click(x=1820, y=917)
                pyautogui.moveTo(x=1853, y=738)
                found = pyautogui.locateOnScreen("./imgs/kingdoms/hesperus.png",confidence = 0.9)
                if(found):
                        done = True
        if(kingdom == "fire"):
                x_p,y_p = 494,808
                file = './towers/firetowers.txt'
                pyautogui.click(x=1826, y=939)
                time.sleep(0.5)
                pyautogui.click(x=1853, y=738)
                found = pyautogui.locateOnScreen("./imgs/kingdoms/esteban.png",confidence = 0.9)
                if(found):
                        done = True
        if(kingdom == "sand"):
                x_p,y_p = 494,808
                file = './towers/sandtowers.txt'
                pyautogui.click(x=1826, y=939)
                time.sleep(0.5)
                pyautogui.click(x=1849, y=760)
                found = pyautogui.locateOnScreen("./imgs/kingdoms/gathalamor.png",confidence = 0.8)
                if(found):
                        done = True
        if(kingdom == "ice"):
                x_p,y_p = 508,831
                file = './towers/icetowers.txt'
                pyautogui.click(x=1826, y=939)
                time.sleep(0.5)
                pyautogui.click(x=1819, y=817)
                found = pyautogui.locateOnScreen("./imgs/kingdoms/farstar.png",confidence = 0.9)
                if(found):
                        done = True
        return x_p,y_p,file,done

def tower_round(x_present,y_present,file):
        towers = []
        total = 0
        with open(file) as f:
                for line in f:
                        x_cord,y_cord = line.split(":")
                        towers.append((x_cord,y_cord))
                        total+=1
        i = 0
        while(i<total):
                repeat = False
                time.sleep(0.5)
                x_cord,y_cord = towers[i][0],towers[i][1]
                pyautogui.doubleClick(x=823,y=90)
                pyautogui.write(x_cord)
                pyautogui.doubleClick(x=876, y=92)
                pyautogui.write(y_cord)
                pyautogui.click(x=942, y=107)
                time.sleep(1)
                pyautogui.click(x=1072, y=591)#attack option
                time.sleep(2)
                cooldown = pyautogui.locateOnScreen("./imgs/cooldown.png",confidence = 0.9)
                if(cooldown):   #check if tower is already attacked
                        pyautogui.click(x=1121, y=747)#leave
                        i+=1
                        continue
                attack = pyautogui.locateOnScreen("./imgs/ok.png",confidence = 0.9)
                if(attack):
                        pyautogui.moveTo(attack)
                        pyautogui.click()
                        #pyautogui.click(x=1089, y=714)#click ok
                        time.sleep(3)
                        #attack screen appears
                        nocommanders = pyautogui.locateOnScreen("./imgs/nocommanders.png",confidence = 0.9)
                        if(nocommanders):
                                val = handle_popups()
                                if(val):
                                        repeat = True
                                if(not repeat):
                                        i+=1  
                                time.sleep(60*(1))
                                continue
                        pyautogui.click(x=554, y=922)#click present
                        time.sleep(1)
                        pyautogui.click(x=x_present, y=y_present)#click present
                        pyautogui.click(x=768, y=924)#click apply all
                        time.sleep(1)
                        pyautogui.click(x=1396, y=980)#click-attack
                        time.sleep(2)
                        attention = pyautogui.locateOnScreen("./imgs/attention.png",confidence = 0.9)
                        if(attention):
                                val = handle_popups()
                                if(val):
                                        repeat = True
                                if(not repeat):
                                        i+=1  
                                time.sleep(60*(1))
                                continue
                        pyautogui.click(x=689, y=543)#coin-horses
                        pyautogui.click(x=1130, y=813)#click ok
                        time.sleep(2)
                val = handle_popups()
                if(val):
                        repeat = True
                if(not repeat):
                        i+=1

time.sleep(2)
found = pyautogui.locateOnScreen("./imgs/worldmap.png",confidence = 0.9)
if found:
        pyautogui.moveTo(found)
        pyautogui.click()
        #we r now on world map
        #hit_kingdom("green")
        #hit_kingdom("ice")
        #time.sleep(1)
        hit_kingdom("fire")
        time.sleep(1)
        hit_kingdom("sand")
        
else:
        #hit_kingdom("green")
        #hit_kingdom("ice")
        #time.sleep(1)
        hit_kingdom("fire")
        time.sleep(1)
        hit_kingdom("sand")

