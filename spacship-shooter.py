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
root.mainloop()