import socket
import tkinter import *
import threading import Thread
import random

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT = 6000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    thread = Thread(target=recivedMsg)
    thread.start()

def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1

    nameWindow = Tk()
    nameWindow.title("Tambola Family Fun")
    nameWindow.geometry('800x600')

    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoIMage(file = "./assets/background.png")

    canvas1 = Canvas(nameWindow, width = 500, height = 500)
    canvas1.pack(fill = "both", expand = True)

    canvas1.create_image(0,0, image = bg, anchor = 'nw')
    canvas1.create_text(screen_width/4.5, screen_height/8, text = "Enter Name", font=("Chalkboard SE",60), fill="black")

    nameEntry = Entry(nameWindow, width = 15, justify='center', font=('Chalkboard SE', 38), bd=5, bg = 'white')
    nameEntry.place(x = screen_width/7, y=screen_height/4)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()

def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())

def createTicket():
    global gameWindow
    global ticketGrid

    mainLabel = Label(gameWindow, width=65, height=16,relief='ridge', borderwidth=5, bg='white')
    mainLabel.place(x=95, y=119)

    xPos = 105
    yPos = 130
    for row in range(0, 3):
        rowList = []
        for col in range(0, 9):
            if (platform.system() == 'Darwin'):
                boxButton = Button(gameWindow,
                font = ("Chalkboard SE", 18),
                borderwidth = 3,
                pady=23,
                padx=23,
                bg="#fff176",
                highlightbackground='#fff176',
                activebackground='#c5ela5')

                boxButton.place(x=xPos, y=yPos)
            else:
                boxButton = tk.Button(gameWindow, font=('Chalkboard SE', 30), width = 3, height = 2, borderwidth = 5, bg = '#fff176')
                boxButton.place(x = xPos, y=yPos)

            rowList.append(boxButton)
            xPos += 64

        ticketGrid.append(rowList)
        xPos = 105
        yPos += 82
    
    def placeNumbers():
        global ticketGrid
        global currentNumberList

        for row in range(0,3):
            randomColList = []
            counter = 0
            white counter <=4:
            randomCol = random.randint(0,8)
            if(randomCol not in randomColList):
                randomColList.append(randomCol)
                counter +=1