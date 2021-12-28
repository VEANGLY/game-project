import tkinter as tk
import random
from winsound import*
import winsound
root = tk.Tk()
root.geometry("1440x1000")
frame = tk.Frame()
canvas = tk.Canvas(frame)
frame.pack(expan=True,fill="both")
frame.master.title("The spacship Allien shooter!")
canvas.pack(expan=True,fill="both")
# ----------------Group-Vairable-----------------------------------------------------------
movetTime = 0
index = 0
sizey = 100 
sizeRectangle = 250
lifeOfSpaceship = ""
capacity = ""
nameOfSpaceship = ""
bulletsOfSpaceship = ""
imageOfSpaceShip = ""
changProperty = ""
madCountry = ""
button = tk.Button( root, text = "EXIT",command=root.destroy)
button.config(height=1,width=11,bg ='#18dcff',font=("Arial",17,"bold"),fg="Orange")
grouptext=["You,are ,my Cruse,but I  don,t love.I'm sorry ,lady!!","I  don,t love.I'm sorry ,lady!!I  don,t love.I'm sorry ,lady!!",
           "You,are ,my Cruse,but I  don,t love.I'm sorry ,lady!!","I  don,t love.I'm sorry ,lady!!I  don,t love.I'm sorry ,lady!!",
           "You,are ,my Cruse,but I  don,t love.I'm sorry ,lady!!","I  don,t love.I'm sorry ,lady!!I  don,t love.I'm sorry ,lady!!",
           "I  don,t love.I'm sorry ,lady!!I  don,t love.I'm sorry ,lady!!","I  don,t love.I'm sorry ,lady!!I  don,t love.I'm sorry ,lady!!",
           "I  don,t love.I'm sorry ,lady!!I  don,t love.I'm sorry ,lady!!","I  don,t love.I'm sorry ,lady!!I  don,t love.I'm sorry ,lady!!",
           "I  don,t love.I'm sorry ,lady!!I  don,t love.I'm sorry ,lady!!","I  don,t love.I'm sorry ,lady!!I  don,t love.I'm sorry ,lady!!"]
# ------------------------------Group image------------------------------------------------
story1 = tk.PhotoImage(file="pic-sources/bg.png")
background_shot = tk.PhotoImage(file="pic-sources/bg.png")
menuImage = tk.PhotoImage(file="pic-sources/menu.png")
skin3= tk.PhotoImage(file="pic-sources/skin-3.png")
skin2= tk.PhotoImage(file="pic-sources/skin-2.png")
skin1= tk.PhotoImage(file="pic-sources/skin-1.png")
smallAlience1 = tk.PhotoImage(file="pic-sources/aircraft.png")
smallAlience2 = tk.PhotoImage(file="pic-sources/ufo.png")
boosAllience = tk.PhotoImage(file="pic-sources/boss-2.png")
dollars = tk.PhotoImage(file="pic-sources/dollar.png")
plus = tk.PhotoImage(file="pic-sources/plus.png")
lifeImage = tk.PhotoImage(file="pic-sources/like.png")
diamond = tk.PhotoImage(file="pic-sources/diamond.png")
ractangle = tk.PhotoImage(file="pic-sources/Rectangle.png")
ractangle2 = tk.PhotoImage(file="pic-sources/Rectangle2.png")
explosion = tk.PhotoImage(file="pic-sources/explosion1.png")
warning = tk.PhotoImage(file="pic-sources/warning.png")
puasedImage = tk.PhotoImage(file="pic-sources/puase.png")
helpImage = tk.PhotoImage(file="pic-sources/help.png")
winWar = tk.PhotoImage(file="pic-sources/win.png")
lostTheWar = tk.PhotoImage(file="pic-sources/lost.png")         
# -------------------------------------------History-Text------------------------------------------- Viner Hand ITC      
def drawtext():
    if index<len(grouptext):
        canvas.create_text(350,sizey ,text= grouptext[index],font=("Arial",15, 'bold'),fill="WHITE")
        canvas.after(100,createText)
        winsound.PlaySound("sound/start-1.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
        canvas.after(1000,startInterface)
    canvas.create_rectangle(sizeRectangle,540,50+sizeRectangle,580,fill="red",outline="#000")
def createText():
    global index,sizey,sizeRectangle
    index += 1
    sizey += 30
    if index%3==0:
        sizeRectangle +=50
    canvas.after(300,drawtext)
def firstInterface():
    canvas.create_image(700,370,imag=story1,anchor="center")
    canvas.create_image(0,0,imag=ractangle2,anchor="nw")
    canvas.create_text(380,510,text="LAODING.....",font=("Arial",30,'bold'),fill="Orange")
    canvas.after(400,drawtext)
firstInterface()
def puasedTheGame(event):
    canvas.delete("puased")
    canvas.create_rectangle(474,204,924,554, fill="",outline="#18dcff")
    canvas.create_image(700,380,image = puasedImage,anchor="center")
    canvas.create_rectangle(540,390,700,450, fill="#18dcff",outline="#18dcff")
    canvas.create_rectangle(540,460,700,520, fill="red",outline="#18dcff")
    canvas.create_rectangle(710,390,870,450, fill="yellow",outline="#18dcff")
    canvas.create_rectangle(710,460,870,520, fill="blue",outline="#18dcff")
    canvas.create_text(790,420,text="RESUME",font=("Arial",20,'bold'),fill="orange",tags="resume")
    canvas.create_text(620,490,text="BACK",font=("Arial",20,'bold'),fill="orange",tags="draw")
    canvas.create_text(790,490,text="HELP",font=("Arial",20,'bold'),fill="orange",tags="help")
    canvas.create_text(620,420,text="NEW",font=("Arial",20,'bold'),fill="orange",tags="start")
# ---------------------Help and delete-------------------------------------------------------
def helpPlayer(event):
    canvas.create_image(600,300,image = helpImage,anchor="center",tags="helping")
    canvas.create_text(390,140,text="<>",font=("Arial",18,'bold'),fill="black",tags="deleteHelp")
def deleteHelper(event):
    canvas.delete("helping")
    canvas.delete("deleteHelp")
def whenWarWin():
    canvas.create_image(600,300,image = winWar,anchor="center",tags="win")
    canvas.create_text(490,430,text="    ",font=("Arial",18,'bold'),fill="black",tags="draw")
    canvas.create_text(610,430,text="    ",font=("Arial",18,'bold'),fill="black",tags="start")
    canvas.create_text(720,430,text="    ",font=("Arial",18,'bold'),fill="black",tags="win")
def whenWarLost():
    canvas.create_image(600,300,image = lostTheWar,anchor="center")
    canvas.create_text(490,430,text="    ",font=("Arial",18,'bold'),fill="black")
    canvas.create_text(610,430,text="    ",font=("Arial",18,'bold'),fill="black")
    canvas.create_text(720,430,text="    ",font=("Arial",18,'bold'),fill="black")
def interfaceInWar(event):
    canvas.delete("all")
    canvas.create_image(0,0,imag=background_shot,anchor="nw")
    canvas.create_rectangle(5,5,140,50, fill="black",outline="#18dcff")
    canvas.create_text(65,35,text="=",font=("Viner Hand ITC",40,'bold'),fill="orange",tags="puased")
    winsound.PlaySound("sound/entro.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.create_rectangle(5,60,140,100, fill="black",outline="#18dcff")
    canvas.create_text(65,80,text=888,font=("Arial",15,'bold'),fill="orange")
    canvas.create_image(24,80,image=dollars)
    canvas.create_rectangle(5,110,140,150, fill="black",outline="#18dcff")
    canvas.create_text(65,130,text=888,font=("Arial",15,'bold'),fill="orange")
    canvas.create_image(24,130,image = lifeImage)
    whenWarWin()
    # explosionDisplay()
    # canvas.after(1000,warnningTime)
# --------------------------------------------Interface----------------------------------------------------
def startInterface():
    button_canvas = canvas.create_window(500, 458, anchor = "nw",window = button)
    canvas.create_image(0,0,imag=background_shot,anchor="nw")
    canvas.create_text(150,50,text="ALLIENC_SLAYER",font=("Viner Hand ITC",15, 'bold'),fill="")
    canvas.create_rectangle(500,320,660,377, fill="#18dcff",outline="")
    canvas.create_text(580,350,text="START",font=("Arial",15, 'bold'),fill="Orange",tags="start")
    canvas.create_rectangle(500,390,660,443, fill="#18dcff",outline="")
    canvas.create_text(580,418,text="MENU",font=("Arial",15, 'bold'),fill="Orange",tags="menu")
# -------------------------Interface draw Again--------------------------------------------
def drawagain(event):
    startInterface()
# -------------------------Interface menu...................................................   
def menuInface(event):
    global skinOne,skinTwo,skinTree,allience1,allience2,allienceBoss,isNotInWar
    canvas.delete("all")
    canvas.create_image(0,0,imag = menuImage,anchor="nw") 
    canvas.create_oval(1040,20,1240,220,fill="#18dcff",outline="#18dcff")
    canvas.create_oval(1050,30,1230,210,fill="black",outline="dark blue")  
    canvas.create_oval(1040,230,1240,430,fill="#18dcff",outline="#18dcff")
    canvas.create_oval(1050,240,1230,420,fill="black",outline="dark blue") 
    canvas.create_oval(1040,440,1240,640,fill="#18dcff",outline="#18dcff")
    canvas.create_oval(1050,450,1230,630,fill="black",outline="dark blue")
    skinOne = canvas.create_image(1150,120,imag=skin3,anchor="center",tags="display3") 
    skinTwo = canvas.create_image(1150,320,imag=skin2,anchor="center",tags="display4")
    skinTree = canvas.create_image(1150,530,imag=skin1,anchor="center",tags="display5")
    canvas.create_oval(300,440,500,640,fill="#18dcff",outline="#18dcff")
    canvas.create_oval(310,450,490,630,fill="black",outline="dark blue") 
    canvas.create_oval(540,440,740,640,fill="#18dcff",outline="#18dcff")
    canvas.create_oval(550,450,730,630,fill="black",outline="dark blue")
    canvas.create_oval(770,440,970,640,fill="#18dcff",outline="#18dcff")
    canvas.create_oval(780,450,960,630,fill="black",outline="dark blue")
    allience1=canvas.create_image(400,540,image=smallAlience1,anchor="center",tags="display1")
    allience2=canvas.create_image(645,540,image=smallAlience2,anchor="center",tags="display2")
    allienceBoss=canvas.create_image(880,530,image=boosAllience,anchor="center",tags="displayboss")  
    canvas.create_rectangle(705,5,955,50, fill="black",outline="dark blue")
    canvas.create_rectangle(505,5,695,50, fill="black",outline="dark blue")
    canvas.create_rectangle(305,5,495,50, fill="black",outline="dark blue")
    canvas.create_image(730,30,image=dollars)
    canvas.create_image(940,30,image=plus)
    canvas.create_image(530,30,image=lifeImage)
    canvas.create_image(680,30,image=plus)
    canvas.create_image(330,30,image=diamond)
    canvas.create_image(480,30,image=plus)
    canvas.create_text(780,30,text="99999",font=("Arial",15, 'bold'),fill="orange")
    canvas.create_text(580,30,text="777",font=("Arial",15, 'bold'),fill="orange")
    canvas.create_text(380,30,text="666",font=("Arial",15, 'bold'),fill="orange")
    canvas.create_rectangle(5,5,140,50, fill="black",outline="#18dcff")
    canvas.create_text(65,30,text="BACK",font=("Viner Hand ITC",15,'bold'),fill="orange",tags="draw")
    activitie2()
#---------------------Allience display------------------------------------------------------------  
def disPlayTemplate():
    winsound.PlaySound("sound/spaceship.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    spaceShipX = canvas.create_image(390,200,image=imageOfSpaceShip ,anchor="nw")
    canvas.create_image(650,100,image=ractangle,anchor="nw")
    canvas.create_text(845,120,text= "CAPACITY",font=("Viner Hand ITC",20, 'bold'),fill="RED")
    canvas.create_text(745,180,text= "LIFE: ",font=("Viner Hand ITC",20, 'bold'),fill="RED")
    canvas.create_text(820,180,text= lifeOfSpaceship ,font=("Aria",20, 'bold'),fill="#18dcff")
    canvas.create_text(760,220,text= changProperty,font=("Viner Hand ITC",20, 'bold'),fill="RED")
    canvas.create_text(880,220,text= capacity,font=("Aria",20, 'bold'),fill="#18dcff")
    canvas.create_text(760,260,text= "NAME: ",font=("Viner Hand ITC",20, 'bold'),fill="RED")
    canvas.create_text(880,260,text= nameOfSpaceship,font=("Aria",20, 'bold'),fill="#18dcff")
    canvas.create_text(760,300,text= "BULLETS: ",font=("Viner Hand ITC",20, 'bold'),fill="RED")
    canvas.create_text(900,300,text= bulletsOfSpaceship,font=("Aria",18, 'bold'),fill="#18dcff")
    canvas.create_text(810,370,text= madCountry,font=("Viner Hand ITC",20, 'bold'),fill="orange")
# -----------------------Spaceship-informaion----------------------------------------------------
def disPlayBoos(event):
    canvas.delete("all")
    global lifeOfSpaceship,capacity,nameOfSpaceship,bulletsOfSpaceship,imageOfSpaceShip,changProperty,madCountry
    menuInface(event)
    lifeOfSpaceship = "x100"
    capacity = "90%"
    nameOfSpaceship = "XWV-95"
    bulletsOfSpaceship = "BOOM-A26"
    imageOfSpaceShip=boosAllience
    changProperty="DANGER"
    madCountry = "MAD IN VEITNAM..!" 
    disPlayTemplate()
def disPlay1(event):
    global lifeOfSpaceship,capacity,nameOfSpaceship,bulletsOfSpaceship,imageOfSpaceShip,changProperty,madCountry
    canvas.delete("all")
    menuInface(event)
    lifeOfSpaceship = "x1"
    capacity = "60%"
    nameOfSpaceship = "XWV-90"
    bulletsOfSpaceship = "BOOM-A10"
    imageOfSpaceShip = smallAlience1
    changProperty="DANGER"
    madCountry = "MAD IN VEITNAM..!"
    disPlayTemplate()
def disPlay2(event):
    global lifeOfSpaceship,capacity,nameOfSpaceship,bulletsOfSpaceship,imageOfSpaceShip,changProperty,madCountry
    canvas.delete("all")
    menuInface(event)
    lifeOfSpaceship = "x2"
    capacity = "80%"
    nameOfSpaceship = "XWV-93"
    bulletsOfSpaceship = "BOOM-A18"
    imageOfSpaceShip = smallAlience2
    changProperty="DANGER"
    madCountry = "MAD IN VEITNAM..!" 
    disPlayTemplate()
def disPlay3(event):
    global lifeOfSpaceship,capacity,nameOfSpaceship,bulletsOfSpaceship,imageOfSpaceShip,changProperty,madCountry
    canvas.delete("all")
    menuInface(event)
    lifeOfSpaceship = "x3"
    capacity = "80%"
    nameOfSpaceship = "XWV-60"
    bulletsOfSpaceship = "BOOM-A19"
    changProperty="KELLED"
    madCountry = "MAD IN CAMBODIA..!"
    imageOfSpaceShip = skin3
    disPlayTemplate()
def disPlay4(event):
    global lifeOfSpaceship,capacity,nameOfSpaceship,bulletsOfSpaceship,imageOfSpaceShip,changProperty,madCountry
    canvas.delete("all")
    menuInface(event)
    lifeOfSpaceship = "x3"
    capacity = "70%"
    nameOfSpaceship = "XWV-A16"
    bulletsOfSpaceship = "BOOM-A11"
    changProperty="KELLED"
    madCountry = "MAD IN CAMBODIA..!"
    imageOfSpaceShip = skin2
    disPlayTemplate()
def disPlay5(event):
    global lifeOfSpaceship,capacity,nameOfSpaceship,bulletsOfSpaceship,imageOfSpaceShip,changProperty,madCountry  
    canvas.delete("all")
    menuInface(event)
    lifeOfSpaceship = "x3"
    capacity = "55%"
    nameOfSpaceship = "XWV-M45"
    bulletsOfSpaceship = "BOOM-A19"
    changProperty="KELLED"
    madCountry = "MAD IN CAMBODIA..!"
    imageOfSpaceShip = skin1
    disPlayTemplate()
#=-------------------------------------Move menu order----------------------------------------------
def activitie():  
    global movetTime,skinOne
    if movetTime < 1:
        canvas.move(skinOne,-5,0)
        canvas.move(skinTwo,-5,0)
        canvas.move(skinTree,-5,0)
        canvas.move(allience1,-5,0)
        canvas.move(allience2,-5,0)
        canvas.move(allienceBoss,-5,0)
        canvas.after(1000,activitie)
        movetTime +=1
    else:
        activitie2()
def activitie2():  
    global movetTime,skinOne
    if movetTime > 0:
        canvas.move(skinOne,5,0)
        canvas.move(skinTwo,5,0)
        canvas.move(skinTree,5,0)
        canvas.move(allience1,5,0)
        canvas.move(allience2,5,0)
        canvas.move(allienceBoss,5,0)
        canvas.after(1000,activitie2)
        movetTime -=1
    else:
        activitie()
# ----------------------Warnninng-Boss------------------------------------------------------
def warnningTime():
    canvas.create_image(300,250,image=warning,anchor="nw")
    winsound.PlaySound("sound/warning.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
# ------------------------------Using-Graphic...............................................
canvas.tag_bind("puased","<Button-1>",puasedTheGame)
canvas.tag_bind("start","<Button-1>",interfaceInWar)
canvas.tag_bind("draw","<Button-1>",drawagain)
canvas.tag_bind("menu","<Button-1>",menuInface)
canvas.tag_bind("displayboss","<Button-1>",disPlayBoos)
canvas.tag_bind("display1","<Button-1>",disPlay1)
canvas.tag_bind("display2","<Button-1>",disPlay2)
canvas.tag_bind("display3","<Button-1>",disPlay3)
canvas.tag_bind("display4","<Button-1>",disPlay4)
canvas.tag_bind("display5","<Button-1>",disPlay5)
canvas.tag_bind("help","<Button-1>",helpPlayer)
canvas.tag_bind("deleteHelp","<Button-1>",deleteHelper)


############################ Game Process/Start Game ##############################

#---------------Human spaceship-------------
skin1Image = tk.PhotoImage(file="pic-sources/skin-1.png")
skin2Image = tk.PhotoImage(file="pic-sources/skin-2.png")
skin3Image = tk.PhotoImage(file="pic-sources/skin-3.png")

# ----------------creat shapeship and bullets and move--------------
# -----------------skin---------------------
skinNumber = 1
humanLife = 3
skin = canvas.create_image(720, 1100, image=skin1Image, anchor="center")
#---------------------------
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
isBullet1 = True
isBullet2 = True
isBullet3 = True
def createBullet1():
    global bullet1, isBullet1, storeBullet
    if isBullet1 and humanLife > 0:
        bullet1 = canvas.create_rectangle(canvas.coords(skin)[0]-4, canvas.coords(skin)[1]-65, canvas.coords(skin)[0]+4, canvas.coords(skin)[1]-105, fill="dark blue", outline="")
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

# #---------------Alien spaceship-------------
bossImage = tk.PhotoImage(file="pic-sources/boss-1.png")
smallAlienImage = tk.PhotoImage(file="pic-sources/small-alien-1.png")

# # ----------------creat boss and small alien--------------
# # -----------------boss---------------------
isBoss = True
def createBoss():
    global boss, bossLife
    bossLife = 100
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
bossExploImage = tk.PhotoImage(file="pic-sources/boss-explosion.png")
def displayBossExplo():
    global bossExplosion
    bossExplosion = canvas.create_image(canvas.coords(boss)[0], canvas.coords(boss)[1], image=bossExploImage, anchor="center")

#-----------------create small alien-------------
smallAlienAmount = 15
indexOfAlien = 0
def createSmallAlien():
    global smallAlien, smallAlienAmount, indexOfAlien, upgrader, smallAlienRanX
    smallAlienRanX = random.randrange(100, 1340)
    if smallAlienAmount > 0:
        smallAlien = canvas.create_image(smallAlienRanX, -50, image=smallAlienImage, anchor="center")
        indexOfAlien += 1
        moveSmallAlien()

#------------------update bullet---------------------
upgradeImage = tk.PhotoImage(file="pic-sources/upgrade-skin.png")
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

# -------------- move boss down----------------------
isBossBlood = False
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
exploImage = tk.PhotoImage(file="pic-sources/explosion.png")
def disExplosion():
    global explosion
    explosion = canvas.create_image(canvas.coords(smallAlien)[0], canvas.coords(smallAlien)[1], image=exploImage, anchor="center")
    canvas.after(149, removeExplo)

#---------------------remove explosion-----------------------
def removeExplo():
    canvas.delete(explosion)

#-----------------explosion small alien----------------
def CheckExplo():
    global forDecrease, smallAlienAmount, bossLife, skinNumber, isBullet1, upgrader, isTargeted, humanSmallExplo, shootedBoss
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

#----------------------get coin---------------------
meduimCoinImage = tk.PhotoImage(file="pic-sources/coin-meduim.png")
smallCoinImage = tk.PhotoImage(file="pic-sources/coin-small.png")
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
    canvas.create_image(canvas.coords(skin)[0], canvas.coords(skin)[1], image=exploImage)
    canvas.delete(skin)

#------------------------human hearts---------------------
heartImage = tk.PhotoImage(file="pic-sources/human-heart.png")
def humanHeart():
    global heart1, heart2, heart3
    heart1 = canvas.create_image(30, 30, image=heartImage, anchor="center")
    heart2 = canvas.create_image(60, 30, image=heartImage, anchor="center")
    heart3 = canvas.create_image(90, 30, image=heartImage, anchor="center")
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

#-------------------------else-------------------
randomUpdateBullet()
createSmallAlien()
randomUpdateBullet()
slideSkin()

root.mainloop()