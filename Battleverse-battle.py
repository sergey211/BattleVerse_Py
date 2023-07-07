# The BattleVerse batlle Python script made by Svetlichny Sergey 
# This test goes with next requirments:
# win 10, resolution 1366x768, 
# On panel there are icons of CMD, Chrome and YaBrowser 
# If icon 'windows' is first, YaBrowser is 4th, Chrome - 6th, CMD - 7th
# Both browsers are opened on page of battle

# Script creates the battle from one player and accept it from seconds
# Then it waits for end of battle and shows who won
# Then repeat this cycle decribed quantity times

# Made with using this source: https://mad-dog.ru/how-to-build-python-bot-web-games/
# To install libraries use:
# python -m pip install pywin32
# python -m pip install numpy
# python -m pip install pyautogui
import pyautogui as pag
from PIL import ImageGrab
import webbrowser
import os
import time
import random
import platform
gameFinished = False
leftwon=0
rightwon=0

# pag.keyDown('win')
# pag.keyDown('tab')
# time.sleep(1)
# pag.keyUp('tab')
# pag.press('tab')
# pag.keyUp('win')

# webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
# webbrowser.get('Chrome').open_new_tab('vk.com')


class Cord10: #for book (version of game with Menu)
    chrom=272,750
    yand=170,750
    cmd=320,750
    lftcrtgm=650,535
    # rtreroll=1273,208
    rtreroll=1280,130
    lftaccpt=528,340
    # rtaccpt=1172,262
    rtaccpt=1177,188
    lftreroll=660,267
    lftcoinplus=500,370
    lftcreate=500,445
    potcoin=413,227
    # potcoin=410,218
    leftOk=440,500
    rghtOk=1110,300
    rightbrsr=1100,15

    lftweapon=300,535
    lfthealth=334,535
    # rgtweapon=919,591
    # rgthealth=943,594
    
    lftblade=372,530
    lftdefence=403,510
    lftstar=435,530
    lftturn=405,545
    

'''
class Cord: #Book (cords without Menu)
    chrom=272,750
    yand=170,750
    cmd=320,750
    lftcrtgm=717,634
    lftaccpt=546,404
    lftcoinplus=515,440
    lftcreate=495,526
    lftreroll=706,314
    rtaccpt=1147,233
    rtcrtgm=1211,340
    rtcoinplus=1128,254
    rtcreate=1120,292
    rtreroll=1216,196
    maxmzleft=720,20
    maxmzrght=1295,15
    potcoin=402,262
    leftOk=435,595
    rghtOk=1100,320

#repair:

    lftweapon=270,650
    lfthealth=310,641
    rgtweapon=1023,344
    rgthealth=1040,345
    
    lftblade=357,637
    lftdefence=395,617
    
    lftstar=436,638
    lftturn=401,656  
'''
class Cord7: #PC
    chrom=214,750
    yand=150,750
    cmd=270,750
    lftcrtgm=670,620
    lftaccpt=550,410
    lftcoinplus=520,440
    lftcreate=505,520
    lftreroll=668,324
    rtaccpt=1145,395
    rtcrtgm=1270,585
    rtcoinplus=1120,430
    rtcreate=1110,500
    rtreroll=1280,320
    # maxmzleft=720,20
    maxmzrght=1290,8
    potcoin=420,280
    leftOk=440,590
    rghtOk=1060,560
    
    lftweapon=290,624
    lfthealth=328,624
    rgtweapon=919,591
    rgthealth=943,594
    
    lftblade=376,622
    lftdefence=410,610
    lftstar=450,622
    lftturn=410,640
'''    
    # lftcancel=
    # lftwaitoppon=
    # lftgreenlives=     
    # rgtgreenlives=     
'''

def screenGrab():
    box = ()
    im = ImageGrab.grab(box)
    # im.save(os.getcwd() + '\\_snap__' + str(int(time.time())) + '.png', 'PNG')

def screenStart(name1):
    box = ()
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\'+name1+'.png', 'PNG')
    print('screenShot '+name1+' saved')
   
def screenGrabPix():
    b1=()  
    im = ImageGrab.grab(b1)
    return im
 
def prepareBrowsers7():    
    pag.moveTo(Cord.yand)
    pag.click()
    pag.keyDown('win')
    time.sleep(1)
    pag.press('left')
    time.sleep(1)
    pag.keyUp('win')
    time.sleep(1)
    pag.press('esc')
    time.sleep(1)
   
    pag.moveTo(Cord.chrom)
    pag.click()
    pag.keyDown('win')
    time.sleep(1)
    pag.press('right')
    time.sleep(1)
    pag.keyUp('win')
    time.sleep(1)
    pag.moveTo(Cord.cmd)
    pag.click()


def prepareBrowsers10():    
    pag.moveTo(Cord.yand) 
    pag.click()
    pag.keyDown('win')
    time.sleep(1)
    pag.press('left')
    time.sleep(1)
    pag.keyUp('win')
    time.sleep(1)
    pag.press('esc')
    time.sleep(1)
    
    pag.moveTo(Cord.chrom) 
    pag.click()
    pag.keyDown('win')
    time.sleep(1)
    pag.press('right')
    time.sleep(1)
    pag.press('up')
    time.sleep(1)
    pag.keyUp('win')
    time.sleep(1)
    pag.press('enter')
    
def startGameLftPlyr():
    im = screenGrabPix()
    # pag.moveTo(500,500,2)
    pag.moveTo(Cord.lftcrtgm)
    time.sleep(1)
    pag.click()
    time.sleep(1)
    pag.moveTo(Cord.lftcoinplus)
    time.sleep(1)
    # pag.click()
    pag.click() # добавим еще 1 монету
    time.sleep(1)
    pag.moveTo(Cord.lftcreate)
    time.sleep(1)
    print('Проверяем кнопку CREATE слева')
    creatButtonRGB = im.getpixel((Cord.lftcreate))
    print(creatButtonRGB)
    if creatButtonRGB!=(19, 35, 41):
        print('завершаем скрипт, так как нету кнопки создать')
        screenStart('Game'+str(1)+'FinishedNoYellowBtn')
        exit(0)
    else:
        print('Желтая кнопка есть')
    pag.click()
    time.sleep(3)
# menu go down    
    pag.moveTo(Cord.rightbrsr) 
    time.sleep(1)
    pag.click()
    time.sleep(0.1)
    pag.press('down')
    time.sleep(0.1)
    pag.press('down')
    time.sleep(0.1)
    pag.press('down')
    time.sleep(0.1)
    pag.press('down')
    time.sleep(0.5)
    pag.moveTo(Cord.rtreroll)
    print('Жмем Reroll')
    time.sleep(1)
    pag.click()
    time.sleep(3)
    pag.moveTo(Cord.rtaccpt) 
    print('Жмем Accept')
    pag.click()
#  end because of menu   
    time.sleep(10)
    
    
def startGameRgtPlyr():
    im = screenGrabPix()
    # pag.moveTo(500,500,2)
    pag.moveTo(Cord.rtcrtgm)
    time.sleep(1)
    pag.click()
    time.sleep(1)
    pag.moveTo(Cord.rtcoinplus)
    time.sleep(1)
    # pag.click()
    # pag.click() # добавим еще 1 монету
    time.sleep(1)
    pag.moveTo(Cord.rtcreate)
    time.sleep(1)
    print('Проверяем кнопку CREATE слева')
    creatButtonRGB = im.getpixel((Cord.lftcreate))
    print(creatButtonRGB)
    if creatButtonRGB!=(19, 35, 41):
        print('завершаем скрипт, так как не видна кнопка "создать"')
        screenStart('Game'+str(1)+'FinishedNoYellowBtn')
        exit(0)
    else:
        print('Желтая кнопка есть')

    pag.click()
    time.sleep(3)
    pag.moveTo(Cord.lftreroll)
    time.sleep(2)
    pag.click()
    time.sleep(15) # ждем 15 сек реального игрока
    pag.moveTo(Cord.lftaccpt)
    pag.click()
    time.sleep(1) 
    print('Нажали акцепт')
    pag.moveTo(Cord.cmd)
    pag.click()
    time.sleep(1)
    
def checkStatusGame():
    global gameFinished, leftwon, rightwon
    while not gameFinished:
        im = screenGrabPix()
        weaponcolor=im.getpixel((Cord.lftweapon))
        # print(weaponcolor)
        # screenStart('Game'+str(1)+'FinishedNoYellowBtn')
        # (222, 113, 16)
        if 230>weaponcolor[0]>210:
            pag.moveTo(Cord.lftweapon)
            pag.click()
            print('weapon pressed')
            time.sleep(0.2)
            number = random.randint(1,3)
            if number==1:
                button=Cord.lftblade
                print('blade')
            elif number==2:
                button=Cord.lftdefence
                print('defence')
            elif number==3:
                button=Cord.lftstar
                print('star')
            pag.moveTo(button)
            pag.click()
            time.sleep(0.2) 
            pag.moveTo(Cord.lftturn)
            pag.click()
            time.sleep(0.2)         
        coincolor=im.getpixel((Cord.potcoin))
        print(coincolor)
        if 190<coincolor[0]<230:
            print('the potcoin is detected')
        elif coincolor[0] == 11:  
            print('the game is just finished, wait some')  
        elif 18<coincolor[0]<25:  
            print('the game is finished, left player won')
            leftwon=leftwon+1
            gameFinished=True
        elif 80<coincolor[0]<110:  
            print('the game is finished, right player won')
            rightwon=rightwon+1
            gameFinished=True
        elif coincolor[0] == 0:  
            print('remove please black window')
        elif coincolor[0] == 255:  
            print('remove please white window')  
        else:
            print('the status of game is unknown')
        print('wait for 5 seconds please..')  
        time.sleep(5)
        # checkStatusGame()
    # print('left won '+str(leftwon)+' times')    
    # print('right won '+str(rightwon)+' times')    

def checkLineBr():
    screenStart('Test Line Between Browser Borders')
    pag.moveTo(1265,365)
    pag.moveTo(790,365,1)
    pag.moveTo(790,65,1)
   
def clickBothOk():
    pag.moveTo(Cord.leftOk) 
    time.sleep(1)
    pag.click()
    time.sleep(1)
# this needed because of "ok" is not unvisible cause of menu:    
    pag.moveTo(Cord.rightbrsr) 
    time.sleep(1)
    pag.click()
    time.sleep(0.1)
    pag.press('down')
    time.sleep(0.1)
    pag.press('down')
    time.sleep(0.1)
    pag.press('down')
    time.sleep(0.1)
    pag.press('down')
    time.sleep(0.5)
# end of unvisible "ok" code    
    pag.moveTo(Cord.rghtOk) 
    time.sleep(1)
    pag.click()
    time.sleep(1)
   
def oneSimpleCycle():  
    time.sleep(5)
    startGameLftPlyr()
    time.sleep(7)
    checkStatusGame()
    clickBothOk()

def gameCycles(j):
    global gameFinished, leftwon, rightwon
    for i in range(1,j+1):
        print('Start Game №'+str(i)+' of '+str(j))
        time.sleep(5)
        startGameLftPlyr()
        time.sleep(7) # 7 seconds before start counting
        checkStatusGame()
        print('left won '+str(leftwon)+' times')    
        print('right won '+str(rightwon)+' times') 
        clickBothOk()
        gameFinished = False
    print(str(j)+' Games Finished')
    pag.moveTo(Cord.cmd)
    pag.click()

# print(platform.win32_ver()[0])
if platform.win32_ver()[0]=='10':
    print('win10')
    Cord=Cord10
    prepareBrowsers=prepareBrowsers10
else:
    print('win7')
    Cord=Cord7
    prepareBrowsers=prepareBrowsers7
    
# screenStart('test1')
prepareBrowsers()
# checkLineBr()
gameCycles(3)
# checkStatusGame()
# oneSimpleCycle()
# time.sleep(30)
       
# (197, 116, 47) - yellow coin
# (11, 35, 49) - notif on coin
# (20, 47, 106) - blue won on coin
# (105, 17, 37) - red lost
# (97, 18, 36)
# (90, 19, 36) - red lost
# (87, 20, 35) - red lost
'''
print('Starting script')
pag.moveTo(500,500,1)
# pag.moveTo(800,800,2,1)
# cords2=450,450
# pag.moveTo(cords2)
# print('cords2 passed')
# time.sleep(1)
cords3=470,470,2
pag.moveTo(400,400,2,pag.easeInQuad)
# pag.moveTo(cords3)
print('cords3 passed')
time.sleep(1)
pag.moveTo(Cord.lftcrtgm)
pag.moveTo(Cord.lftcreate,duration=0.2)
print('cords4 passed')
time.sleep(1)
pag.moveTo(Cord.rtaccpt)
pag.moveTo(Cord.rtaccpt,duration=0.2)
pag.moveTo(Cord.rtaccpt,2,pag.easeInOutQuad)
# print('hi')
'''