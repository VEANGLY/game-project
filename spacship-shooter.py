import tkinter as tk
import random
from tkinter.font import BOLD
root = tk.Tk()
root.geometry("1440x1000")
frame = tk.Frame()
canvas = tk.Canvas(frame)
frame.pack(expan=True,fill="both")
frame.master.title("The spacship Allien shooter!")
canvas.pack(expan=True,fill="both")

#------------variables block / images-------------------------------
informLostImage = tk.PhotoImage(file="pic-sources/inform-lost.png")
skin1Image = tk.PhotoImage(file="pic-sources/skin-1.png")
skin2Image = tk.PhotoImage(file="pic-sources/skin-2.png")
skin3Image = tk.PhotoImage(file="pic-sources/skin-3.png")
informWinImage = tk.PhotoImage(file="pic-sources/inform-win.png")
bossImage = tk.PhotoImage(file="pic-sources/boss-1.png")
smallAlienImage = tk.PhotoImage(file="pic-sources/small-alien-1.png")
meduimCoinImage = tk.PhotoImage(file="pic-sources/coin-meduim.png")
smallCoinImage = tk.PhotoImage(file="pic-sources/coin-small.png")
exploImage = tk.PhotoImage(file="pic-sources/explosion.png")
upgradeImage = tk.PhotoImage(file="pic-sources/upgrade-skin.png")
bossExploImage = tk.PhotoImage(file="pic-sources/boss-explosion.png")
heartImage = tk.PhotoImage(file="pic-sources/human-heart.png")
coinsImage = tk.PhotoImage(file="pic-sources/coins.png")
bgImage = tk.PhotoImage(file="pic-sources/bg.png")
lostImage = tk.PhotoImage(file="pic-sources/bg-lost.png")
winImage = tk.PhotoImage(file="pic-sources/bg-win.png")
storeCoin = 0
isNotGame1 = False
#----------------------------first spaceship------------------------
def spaceShip1():
    global skin
    skin = canvas.create_image(720, 1100, image=skin1Image, anchor="center")

#-----------------------start button------------------------------
def startButton():
    global buttonStart, buttonText
    buttonStart = canvas.create_rectangle(650, 470, 790, 530, fill="teal", tags="start")
    buttonText = canvas.create_text(720, 500, text="START", font=("serif", 16, BOLD), fill="cyan", tags="start")

#------------------------------create interface/ background--------------------------------
def firstInterface(event):
    global skinNumber, humanLife, isHuman, skin, isBoss, bossLife, isHumanWin
#-----------------------
    if isNotGame1:
        if not isHumanWin:
            canvas.delete(lostInterface)
            canvas.delete(lostInform)
            canvas.delete(lostScore)
        elif isHumanWin:
            canvas.delete(winInterface)
            canvas.delete(winInform)
            canvas.delete(winScore)
#-----------------------
    isHumanWin = False
    if isNotGame1:
        canvas.delete(homeButton)
        canvas.delete(restartButton)
    canvas.create_image(0, 0, image=bgImage, anchor="nw")
    startButton()

#------------------------start game---------------------------
def startGame(event):
    global storeCoin, isBoss, bossLife, skinNumber, humanLife, isHuman, isBullet1, isBullet2, isBullet3, indexOfAlien, isBossBlood, smallAlienAmount
#-----------------------
    if isNotGame1:
        if not isHumanWin:
            canvas.delete(lostInterface)
            canvas.delete(lostInform)
            canvas.delete(lostScore)
        elif isHumanWin:
            canvas.delete(winInterface)
            canvas.delete(winInform)
            canvas.delete(winScore)
    if isNotGame1:
        canvas.create_image(0, 0, image=bgImage, anchor="nw")
    storeCoin = 0
#-----------------------
    isBoss = True
    bossLife = 100
    skinNumber = 1
    humanLife = 3
    isHuman = True
    isBullet1 = True
    isBullet2 = True
    isBullet3 = True
    indexOfAlien = 0
    isBossBlood = False
    smallAlienAmount = 15
    canvas.delete(buttonStart)
    canvas.delete(buttonText)
    if isNotGame1:
        canvas.delete(homeButton)
        canvas.delete(restartButton)
    spaceShip1()
    randomUpdateBullet()
    createSmallAlien()
    randomUpdateBullet()
    slideSkin()

#-----------------------home--------------------------------
def backHome():
    global homeButton
    if humanLife <= 0:
        homeButton = canvas.create_rectangle(605, 605, 700, 665, fill="", outline="", tags="home")
    elif bossLife <= 0:
        homeButton = canvas.create_rectangle(570, 605, 665, 665, fill="", outline="", tags="home")

#-----------------------restart-----------------------------
def restartGame():
    global restartButton
    if humanLife <= 0:
        restartButton = canvas.create_rectangle(745, 605, 835, 665, fill="", outline="", tags="restart")
    elif bossLife <= 0:
        restartButton = canvas.create_rectangle(690, 605, 780, 665, fill="", outline="", tags="restart")

#--------------------lost game-------------------------------
def gameLost():
    global lostInterface, lostInform, lostScore, isNotGame1
    isNotGame1 = True
    lostInterface = canvas.create_image(720, 500, image=lostImage, anchor="center")
    lostInform = canvas.create_image(720, 500, image=informLostImage, anchor="center")
    lostScore = canvas.create_text(750, 510, text=storeCoin, font=("serif", 16, BOLD), fill="red")
    backHome()
    restartGame()
    canvas.tag_bind("home", "<Button-1>", firstInterface)
    canvas.tag_bind("restart", "<Button-1>", startGame)

#--------------------lost game-------------------------------
def gameWin():
    global winInterface, winInform, winScore, isNotGame1
    isNotGame1 = True
    winInterface = canvas.create_image(720, 500, image=winImage, anchor="center")
    winInform = canvas.create_image(720, 500, image=informWinImage, anchor="center")
    winScore = canvas.create_text(750, 518, text=storeCoin, font=("serif", 16, BOLD), fill="yellow")
    backHome()
    restartGame()
    canvas.tag_bind("home", "<Button-1>", firstInterface)
    canvas.tag_bind("restart", "<Button-1>", startGame)

# ----------------creat shapeship and bullets and move--------------
# -----------------skin---------------------
def slideSkin():
    if canvas.coords(skin)[1] > 880:
        canvas.move(skin, 0, -1)
        canvas.after(5, slideSkin)
    else:
        humanHeart()
        createBullet1()
        moveBullet()

#---------------------------change skin------------------------------------
def createSkin():
    global skin, skinPositX, skinPositY
    if skinNumber == 2:
        canvas.itemconfig(skin, image=skin2Image)
    if skinNumber == 3:
        canvas.itemconfig(skin, image=skin3Image)


#----------------------upgrade spaceship----------------------------
def checkUpgradeSpaceship():
    global skinNumber, isBullet1, isUpgrade, isBullet2
    if bossLife > 0:
        if isUpgrade and canvas.coords(upgrader)[0] < canvas.coords(skin)[0]+60 and canvas.coords(upgrader)[0] > canvas.coords(skin)[0]-60 and canvas.coords(upgrader)[1] > canvas.coords(skin)[1]-60 and canvas.coords(upgrader)[1] < canvas.coords(skin)[1]:
            if skinNumber == 1:
                isUpgrade = False
                skinNumber += 1
                isBullet1 = False
                removeUpgrade()
                removeBullet1()
                createSkin()
                createBullet2()
                randomUpdateBullet()
            elif skinNumber == 2:
                isUpgrade = False
                skinNumber += 1
                isBullet2 = False
                removeUpgrade()
                removeBullet2()
                createSkin()
                createBullet3()
        else:
            canvas.after(1, checkUpgradeSpaceship)
    
#---------------------remove upgrade---------------------
def removeUpgrade():
    global isUpgrade
    canvas.delete(upgrader)
    isUpgrade = False

def moveUpgrader():
    if isUpgrade:
        if canvas.coords(upgrader)[1] < 1020:
            canvas.move(upgrader, 0, 1)
        else:
            removeUpgrade()
            randomUpdateBullet()
    canvas.after(15, moveUpgrader)

#----------------bullet--------------------
def createBullet1():
    global bullet1, isBullet1, storeBullet
    if isBullet1 and humanLife > 0:
        bullet1 = canvas.create_rectangle(canvas.coords(skin)[0]-4, canvas.coords(skin)[1]-65, canvas.coords(skin)[0]+4, canvas.coords(skin)[1]-105, fill="cyan", outline="")
    storeBullet = bullet1

def createBullet2():
    global bullet2, isBullet2, bullet3
    if isBullet2 and humanLife > 0:
        bullet2 = canvas.create_rectangle(canvas.coords(skin)[0]-10, canvas.coords(skin)[1]-100, canvas.coords(skin)[0]-2, canvas.coords(skin)[1]-60, fill="dark orange", outline="")
        bullet3 = canvas.create_rectangle(canvas.coords(skin)[0]+10, canvas.coords(skin)[1]-100, canvas.coords(skin)[0]+2, canvas.coords(skin)[1]-60, fill="dark orange", outline="")

def createBullet3():
    global bullet4, isBullet3, bullet5, bullet6
    if isBullet3 and humanLife > 0:
        bullet4 = canvas.create_rectangle(canvas.coords(skin)[0]-8, canvas.coords(skin)[1]-70, canvas.coords(skin)[0]-16, canvas.coords(skin)[1]-110, fill="teal", outline="")
        bullet5 = canvas.create_rectangle(canvas.coords(skin)[0]-4, canvas.coords(skin)[1]-70, canvas.coords(skin)[0]+4, canvas.coords(skin)[1]-110, fill="teal", outline="")
        bullet6 = canvas.create_rectangle(canvas.coords(skin)[0]+8, canvas.coords(skin)[1]-70, canvas.coords(skin)[0]+16, canvas.coords(skin)[1]-110, fill="teal", outline="")

# ----------------move bullet--------------------
def moveBullet():
    global storeBullet
    if isBoss and humanLife > 0:
        if skinNumber == 1:
            canvas.move(bullet1, 0, -3)
            storeBullet = bullet1
            if canvas.coords(bullet1)[1] < -40:
                createBullet1()
        if skinNumber == 2:
            canvas.move(bullet2, 0, -3)
            canvas.move(bullet3, 0, -3)
            storeBullet = bullet2
            if canvas.coords(bullet2)[1] < -40 or canvas.coords(bullet3)[1] < -40:
                createBullet2()
        if skinNumber == 3:
            canvas.move(bullet4, 0, -3)
            canvas.move(bullet5, 0, -3)
            canvas.move(bullet6, 0, -3)
            storeBullet = bullet5
            if canvas.coords(bullet4)[1] < -40 or canvas.coords(bullet5)[1] < -40 or canvas.coords(bullet6)[1] < -40:
                createBullet3()
        CheckExplo()
        canvas.after(1, moveBullet)

#----------------delete bullet--------------------
#--------delete bullet 1----------
def removeBullet1():
    canvas.delete(bullet1)
    canvas.delete(storeBullet)
    createBullet1()

#--------delete bullet 2---------
def removeBullet2():
    canvas.delete(bullet2)
    canvas.delete(bullet3)
    canvas.delete(storeBullet)
    createBullet2()

#--------delete bullet 3---------
def removeBullet3():
    canvas.delete(bullet4)
    canvas.delete(bullet5)
    canvas.delete(bullet6)
    canvas.delete(storeBullet)
    createBullet3()

# # ----------------creat boss and small alien--------------
# # -----------------boss---------------------
def createBoss():
    global boss
    boss = canvas.create_image(720, -150, image=bossImage, anchor="center")
    moveBossDown()

#--------------------boss bullets------------------------
def createBossBullet():
    global bossBullet1, bossBullet2, bossBullet3, bossBullet4, bossBullet5, bossBullet6, bossBullet7, bossBullet8, isBossBullet1, isBossBullet2, isBossBullet3, isBossBullet4, isBossBullet5, isBossBullet6, isBossBullet7, isBossBullet8
    bossBullet1 = canvas.create_oval(canvas.coords(boss)[0]-115, canvas.coords(boss)[1]+50, canvas.coords(boss)[0]-100, canvas.coords(boss)[1]+65, fill="red", outline="")
    bossBullet2 = canvas.create_oval(canvas.coords(boss)[0]-115, canvas.coords(boss)[1]+50, canvas.coords(boss)[0]-100, canvas.coords(boss)[1]+65, fill="red", outline="")
    bossBullet3 = canvas.create_oval(canvas.coords(boss)[0]-75, canvas.coords(boss)[1]+115, canvas.coords(boss)[0]-60, canvas.coords(boss)[1]+130, fill="red", outline="")
    bossBullet4 = canvas.create_oval(canvas.coords(boss)[0]-75, canvas.coords(boss)[1]+115, canvas.coords(boss)[0]-60, canvas.coords(boss)[1]+130, fill="red", outline="")
    bossBullet5 = canvas.create_oval(canvas.coords(boss)[0]+75, canvas.coords(boss)[1]+115, canvas.coords(boss)[0]+60, canvas.coords(boss)[1]+130, fill="red", outline="")
    bossBullet6 = canvas.create_oval(canvas.coords(boss)[0]+75, canvas.coords(boss)[1]+115, canvas.coords(boss)[0]+60, canvas.coords(boss)[1]+130, fill="red", outline="")
    bossBullet7 = canvas.create_oval(canvas.coords(boss)[0]+115, canvas.coords(boss)[1]+50, canvas.coords(boss)[0]+100, canvas.coords(boss)[1]+65, fill="red", outline="")
    bossBullet8 = canvas.create_oval(canvas.coords(boss)[0]+115, canvas.coords(boss)[1]+50, canvas.coords(boss)[0]+100, canvas.coords(boss)[1]+65, fill="red", outline="")
    isBossBullet1 = True
    isBossBullet2 = True
    isBossBullet3 = True
    isBossBullet4 = True
    isBossBullet5 = True
    isBossBullet6 = True
    isBossBullet7 = True
    isBossBullet8 = True

#---------------------move boss bullet--------------------
def moveBossBullet():
    global humanLife, shootedHuman
    if humanLife > 0 and bossLife > 0:
        if isBossBullet1:
            canvas.move(bossBullet1, -1, +1.5)
        if isBossBullet2:
            canvas.move(bossBullet2, +1, +1.5)
        if isBossBullet3:
            canvas.move(bossBullet3, -1, +1.5)
        if isBossBullet4:
            canvas.move(bossBullet4, 0, +1.5)
        if isBossBullet5:
            canvas.move(bossBullet5, 0, +1.5)
        if isBossBullet6:
            canvas.move(bossBullet6, +1, +1.5)
        if isBossBullet7:
            canvas.move(bossBullet7, -1, +1.5)
        if isBossBullet8:
            canvas.move(bossBullet8, +1, +1.5)
        checkHumanExplo()
        if isBossBullet8:
            if canvas.coords(bossBullet8)[1] > 1200:
                createBossBullet()
        elif isBossBullet1:
            if canvas.coords(bossBullet1)[1] > 1200:
                createBossBullet()
        canvas.after(10, moveBossBullet)
    elif humanLife <= 0:
        humanExplo()
        canvas.after(1000, gameLost)

#-------------------------remove human little explo---------------
shootedHuman = tk.PhotoImage(file="pic-sources/little-explo.png")
def deleteHumanSE():
    canvas.delete(humanSmallExplo)

#-----------------------remove boss small explo----------------
def deleteBossSE():
    canvas.delete(bossSmallExplo)

#------------------check human explosion-------------------
def checkHumanExplo():
        global humanSmallExplo, humanLife, isBossBullet1, isBossBullet2, isBossBullet3, isBossBullet4, isBossBullet5, isBossBullet6, isBossBullet7, isBossBullet8
        if isBossBullet1:
            if canvas.coords(bossBullet1)[0] < canvas.coords(skin)[0]+64 and canvas.coords(bossBullet1)[0] > canvas.coords(skin)[0]-64 and canvas.coords(bossBullet1)[1] > canvas.coords(skin)[1]-64 and canvas.coords(bossBullet1)[1] < canvas.coords(skin)[1]+40:
                humanLife -= 1
                isBossBullet1 = False
                humanSmallExplo = canvas.create_image(canvas.coords(bossBullet1)[0], canvas.coords(bossBullet1)[1], image=shootedHuman, anchor="center")
                canvas.delete(bossBullet1)
                canvas.after(100, deleteHumanSE)
        if isBossBullet2:
            if canvas.coords(bossBullet2)[0] < canvas.coords(skin)[0]+64 and canvas.coords(bossBullet2)[0] > canvas.coords(skin)[0]-64 and canvas.coords(bossBullet2)[1] > canvas.coords(skin)[1]-64 and canvas.coords(bossBullet2)[1] < canvas.coords(skin)[1]+40:
                humanLife -= 1
                isBossBullet2 = False
                humanSmallExplo = canvas.create_image(canvas.coords(bossBullet2)[0], canvas.coords(bossBullet2)[1], image=shootedHuman, anchor="center")
                canvas.delete(bossBullet2)
                canvas.after(100, deleteHumanSE)
        if isBossBullet3:
            if canvas.coords(bossBullet3)[0] < canvas.coords(skin)[0]+64 and canvas.coords(bossBullet3)[0] > canvas.coords(skin)[0]-64 and canvas.coords(bossBullet3)[1] > canvas.coords(skin)[1]-64 and canvas.coords(bossBullet3)[1] < canvas.coords(skin)[1]+40:
                humanLife -= 1
                isBossBullet3 = False
                humanSmallExplo = canvas.create_image(canvas.coords(bossBullet3)[0], canvas.coords(bossBullet3)[1], image=shootedHuman, anchor="center")
                canvas.delete(bossBullet3)
                canvas.after(100, deleteHumanSE)
        if isBossBullet4:
            if canvas.coords(bossBullet4)[0] < canvas.coords(skin)[0]+64 and canvas.coords(bossBullet4)[0] > canvas.coords(skin)[0]-64 and canvas.coords(bossBullet4)[1] > canvas.coords(skin)[1]-64 and canvas.coords(bossBullet4)[1] < canvas.coords(skin)[1]+40:
                humanLife -= 1
                isBossBullet4 = False
                humanSmallExplo = canvas.create_image(canvas.coords(bossBullet4)[0], canvas.coords(bossBullet4)[1], image=shootedHuman, anchor="center")
                canvas.delete(bossBullet4)
                canvas.after(100, deleteHumanSE)
        if isBossBullet5:
            if canvas.coords(bossBullet5)[0] < canvas.coords(skin)[0]+64 and canvas.coords(bossBullet5)[0] > canvas.coords(skin)[0]-64 and canvas.coords(bossBullet5)[1] > canvas.coords(skin)[1]-64 and canvas.coords(bossBullet5)[1] < canvas.coords(skin)[1]+40:
                humanLife -= 1
                isBossBullet5 = False
                humanSmallExplo = canvas.create_image(canvas.coords(bossBullet5)[0], canvas.coords(bossBullet5)[1], image=shootedHuman, anchor="center")
                canvas.delete(bossBullet5)
                canvas.after(100, deleteHumanSE)
        if isBossBullet6:
            if canvas.coords(bossBullet6)[0] < canvas.coords(skin)[0]+64 and canvas.coords(bossBullet6)[0] > canvas.coords(skin)[0]-64 and canvas.coords(bossBullet6)[1] > canvas.coords(skin)[1]-64 and canvas.coords(bossBullet6)[1] < canvas.coords(skin)[1]+40:
                humanLife -= 1
                isBossBullet6 = False
                humanSmallExplo = canvas.create_image(canvas.coords(bossBullet6)[0], canvas.coords(bossBullet6)[1], image=shootedHuman, anchor="center")
                canvas.delete(bossBullet6)
                canvas.after(100, deleteHumanSE)
        if isBossBullet7:
            if canvas.coords(bossBullet7)[0] < canvas.coords(skin)[0]+64 and canvas.coords(bossBullet7)[0] > canvas.coords(skin)[0]-64 and canvas.coords(bossBullet7)[1] > canvas.coords(skin)[1]-64 and canvas.coords(bossBullet7)[1] < canvas.coords(skin)[1]+40:
                humanLife -= 1
                isBossBullet7 = False
                humanSmallExplo = canvas.create_image(canvas.coords(bossBullet7)[0], canvas.coords(bossBullet7)[1], image=shootedHuman, anchor="center")
                canvas.delete(bossBullet7)
                canvas.after(100, deleteHumanSE)
        if isBossBullet8:
            if canvas.coords(bossBullet8)[0] < canvas.coords(skin)[0]+64 and canvas.coords(bossBullet8)[0] > canvas.coords(skin)[0]-64 and canvas.coords(bossBullet8)[1] > canvas.coords(skin)[1]-64 and canvas.coords(bossBullet8)[1] < canvas.coords(skin)[1]+40:
                humanLife -= 1
                isBossBullet8 = False
                humanSmallExplo = canvas.create_image(canvas.coords(bossBullet8)[0], canvas.coords(bossBullet8)[1], image=shootedHuman, anchor="center")
                canvas.delete(bossBullet8)
                canvas.after(100, deleteHumanSE)
        decreaseHeart()
        


#------------------remove happend-----------------------
def removeBoss():
    global isBoss
    canvas.delete(boss)
    isBoss = False

#-----------------------boss explosion-----------------
def displayBossExplo():
    global bossExplosion
    bossExplosion = canvas.create_image(canvas.coords(boss)[0], canvas.coords(boss)[1], image=bossExploImage, anchor="center")

#-----------------create small alien-------------
def createSmallAlien():
    global smallAlien, smallAlienAmount, indexOfAlien, upgrader, smallAlienRanX
    smallAlienRanX = random.randrange(100, 1340)
    if smallAlienAmount > 0 and humanLife > 0:
        smallAlien = canvas.create_image(smallAlienRanX, -50, image=smallAlienImage, anchor="center")
        indexOfAlien += 1
        moveSmallAlien()

#------------------update bullet---------------------
def randomUpdateBullet():
    global upgradeNumber, isUpgrade, upgrader
    upgrader = canvas.create_image(0, 0, image="", anchor="center")
    isUpgrade = True
    if skinNumber == 1:
        upgradeNumber = random.randrange(indexOfAlien+1, indexOfAlien+3)
    elif skinNumber == 2:
        upgradeNumber = random.randrange(indexOfAlien, indexOfAlien+5)

#-----------------remove small alien-----------------
def removeSmallAlien():
    canvas.delete(smallAlien)
    if smallAlienAmount > 0:
        createSmallAlien()

#----------------move small alien---------------
def moveSmallAlien():
    global humanLife
    canvas.move(smallAlien, 0, +1)
    if smallAlienAmount > 0:
        if canvas.coords(smallAlien)[1] > 1040:
            humanLife -= 1
            decreaseHeart()
            createSmallAlien()
        canvas.after(90, moveSmallAlien)
        if humanLife <= 0 and isHuman:
            humanExplo()
            canvas.after(1000, gameLost)

# -------------- move boss down----------------------
def moveBossDown():
    global bossBlood, bossBloodBorder, isBossBlood, forDecrease, startedPoint
    if canvas.coords(boss)[1] < 150:
        canvas.move(boss, 0, +1)
        canvas.after(5, moveBossDown)
    else:
        bossBloodBorder = canvas.create_rectangle(canvas.coords(boss)[0]-150, canvas.coords(boss)[1]-135, canvas.coords(boss)[0]+150, canvas.coords(boss)[1]-145, fill="")
        bossBlood = canvas.create_rectangle(canvas.coords(boss)[0]-150, canvas.coords(boss)[1]-135, canvas.coords(boss)[0]+150, canvas.coords(boss)[1]-145, fill="red", outline="")
        startedPoint = canvas.coords(boss)[0]-150
        forDecrease = 300
        isBossBlood = True
        canvas.after(1000, createBossBullet)
        canvas.after(1001, moveBossBullet)
        canvas.after(500, moveBossRight)

#--------------------decrease boss blood-------------------
def decreaseBossBlood():
    global bossBlood
    if isBoss and humanLife > 0:
        if bossLife > 0:
            canvas.delete(bossBlood)
            bossBlood = canvas.create_rectangle(startedPoint, canvas.coords(boss)[1]-135, startedPoint+forDecrease, canvas.coords(boss)[1]-145, fill="red", outline="")
        elif bossLife < 0:
            canvas.delete(bossBlood)
            bossBlood = canvas.create_rectangle(canvas.coords(boss)[0]-150, canvas.coords(boss)[1]-135, canvas.coords(boss)[0]-150, canvas.coords(boss)[1]-145, fill="")

# -------------- move boss right----------------------
def moveBossRight():
    global startedPoint
    if bossLife > 0 and humanLife > 0:
        if canvas.coords(boss)[0] < 1320:
            canvas.move(boss, +1, 0)
            canvas.move(bossBlood, +1, 0)
            canvas.move(bossBloodBorder, +1, 0)
            startedPoint += 1
            canvas.after(10, moveBossRight)
        else:
            canvas.after(10, moveBossback)

# -------------- move boss left----------------------
def moveBossback():
    global startedPoint
    if bossLife > 0 and humanLife > 0:
        if canvas.coords(boss)[0] > 120:
            canvas.move(boss, -1, 0)
            canvas.move(bossBlood, -1, 0)
            canvas.move(bossBloodBorder, -1, 0)
            startedPoint -= 1
            canvas.after(10, moveBossback)
        else:
            canvas.after(10, moveBossRight)

#------------------explosion----------------------------
#-------------------display explosion----------------------
def disExplosion():
    global explosion
    explosion = canvas.create_image(canvas.coords(smallAlien)[0], canvas.coords(smallAlien)[1], image=exploImage, anchor="center")
    canvas.after(149, removeExplo)

#---------------------remove explosion-----------------------
def removeExplo():
    canvas.delete(explosion)

#-----------------explosion small alien----------------
def CheckExplo():
    global isHumanWin, storeCoin, forDecrease, smallAlienAmount, bossLife, skinNumber, isBullet1, upgrader, isTargeted, humanSmallExplo, shootedBoss
    shootedBoss = 0
    isTargeted = False
    if isBoss:
        if smallAlienAmount > 0:
            if canvas.coords(storeBullet)[0] > canvas.coords(smallAlien)[0]-50 and canvas.coords(storeBullet)[0] < canvas.coords(smallAlien)[0]+40 and canvas.coords(storeBullet)[1] > canvas.coords(smallAlien)[1]-35 and canvas.coords(storeBullet)[1] < canvas.coords(smallAlien)[1]:
                isTargeted = True
                disExplosion()
                getCoins()
                if indexOfAlien == upgradeNumber:
                    upgrader = canvas.create_image(canvas.coords(smallAlien)[0], canvas.coords(smallAlien)[1], image=upgradeImage, anchor="center")
                    moveUpgrader()
                    checkUpgradeSpaceship()
            if isTargeted:
                smallAlienAmount -= 1
                removeSmallAlien()
                storeCoin += 50
                increaseCoins()
            if smallAlienAmount == 0:
                createBoss()
        elif bossLife > 0:
            global bossSmallExplo
            if canvas.coords(storeBullet)[0] > canvas.coords(boss)[0]-125 and canvas.coords(storeBullet)[0] < canvas.coords(boss)[0]+125 and canvas.coords(storeBullet)[1] > canvas.coords(boss)[1]-50 and canvas.coords(storeBullet)[1] < canvas.coords(boss)[1]+10:
                if skinNumber == 1:
                    shootedBoss = 1
                    bossSmallExplo = canvas.create_image(canvas.coords(bullet1)[0], canvas.coords(bullet1)[1], image=shootedHuman, anchor="center")
                    canvas.after(100, deleteBossSE)
                elif skinNumber == 2:
                    shootedBoss = 2
                    bossSmallExplo = canvas.create_image(canvas.coords(bullet2)[0]+2, canvas.coords(bullet2)[1], image=shootedHuman, anchor="center")
                    canvas.after(100, deleteBossSE)
                elif skinNumber == 3:
                    shootedBoss = 3
                    bossSmallExplo = canvas.create_image(canvas.coords(bullet5)[0], canvas.coords(bullet5)[1], image=shootedHuman, anchor="center")
                    canvas.after(100, deleteBossSE)
                bossLife -= shootedBoss
                if isBossBlood:
                    forDecrease -= shootedBoss*3
                    decreaseBossBlood()
        elif bossLife <= 0:
            canvas.delete(bossBloodBorder)
            canvas.delete(bossBlood)
            displayBossExplo()
            removeBoss()
            canvas.after(1000, gameWin)
            isHumanWin = True
        if isTargeted or shootedBoss > 0:
            if skinNumber == 1:
                removeBullet1()
            elif skinNumber == 2:
                removeBullet2()
            elif skinNumber == 3:
                removeBullet3()

# #-----------------move human spaceship----------------
#------------------move left---------------------
def moveSpaceShipLeft(event):
    if isBoss and humanLife > 0:
        if canvas.coords(skin)[0] > 100:
            canvas.move(skin, -20, 0)

#------------------move right---------------------
def moveSpaceShipRight(event):
    if isBoss and humanLife > 0:
        if canvas.coords(skin)[0] < 1340:
            canvas.move(skin, +20, 0)

#------------------move up---------------------
def moveSpaceShipUp(event):
    if isBoss and humanLife > 0:
        if canvas.coords(skin)[1] > 500:
            canvas.move(skin, 0, -20)

#------------------move down---------------------
def moveSpaceShipDown(event):
    if isBoss and humanLife > 0:
        if canvas.coords(skin)[1] < 880:
            canvas.move(skin, 0, +20)

#------------------------coins---------------------
def increaseCoins():
    canvas.itemconfig(coinsAmount, text=storeCoin)

#----------------------get coin---------------------
def getCoins():
    global coin1, coin2, coin3
    coin1 = canvas.create_image(smallAlienRanX-25, canvas.coords(smallAlien)[1]-30, image=meduimCoinImage, anchor="center")
    coin2 = canvas.create_image(smallAlienRanX-50, canvas.coords(smallAlien)[1]+35, image=smallCoinImage, anchor="center")
    coin3 = canvas.create_image(smallAlienRanX+30, canvas.coords(smallAlien)[1], image=meduimCoinImage, anchor="center")
    canvas.after(149, removeCoin)

#------------------remove coin-----------------------
def removeCoin():
    canvas.delete(coin1)
    canvas.delete(coin2)
    canvas.delete(coin3)

#-----------------------human explosion------------------------------
def humanExplo():
    global isHuman
    canvas.create_image(canvas.coords(skin)[0], canvas.coords(skin)[1], image=exploImage)
    canvas.delete(skin)
    isHuman = False

#------------------------human hearts and coin---------------------
def humanHeart():
    global heart1, heart2, heart3, coins, coinsAmount
    heart1 = canvas.create_image(30, 30, image=heartImage, anchor="center")
    heart2 = canvas.create_image(60, 30, image=heartImage, anchor="center")
    heart3 = canvas.create_image(90, 30, image=heartImage, anchor="center")
    coins = canvas.create_image(30, 70, image=coinsImage, anchor="center")
    coinsAmount = canvas.create_text(70, 70, text="0", font=("serif", 15), fill="yellow")
def decreaseHeart():
    if isBoss:
        if humanLife == 2:
            canvas.delete(heart3)
        if humanLife == 1:
            canvas.delete(heart2)
        if humanLife == 0:
            canvas.delete(heart1)

#----------------controller-----------------
root.bind("<Left>", moveSpaceShipLeft)
root.bind("<Right>", moveSpaceShipRight)
root.bind("<Up>", moveSpaceShipUp)
root.bind("<Down>", moveSpaceShipDown)

#---------------------buttons--------------------
canvas.tag_bind("start", "<Button-1>", startGame)
firstInterface(0)
root.mainloop()