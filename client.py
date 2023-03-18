import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import font

PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name = None
listbox =  None
textarea= None
labelchat = None
text_message = None

def musicWindow():
   
    print("\n\t\t\t\tMUSIC SHARING APP ")

    window=Tk()

    window.title('MUSIC SHARING APP')
    window.geometry("500x350")

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    Selectsong = Label(window, text= "Select Song ", font = ("Calibri",10))
    Selectsong .place(x=10, y=8)

    listbox = Listbox(window,height = 5,width = 67,activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=70)
    
    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    Play = Button(window,text="Play",bd=1, font = ("Calibri",10))
    Play.place(x=350,y=6)

    Stop=Button(window,text="Stop",bd=1, font = ("Calibri",10))
    Stop.place(x=282,y=160)

    Upload=Button(window,text="Upload",bd=1, font = ("Calibri",10))
    Upload.place(x=350,y=160)

    Download =Button(window,text="Download ",bd=1, font = ("Calibri",10))
    Download .place(x=435,y=160)

    Infolabel = Label(window, text= "",fg='blue' ,font = ("Calibri",8))
    Infolabel .place(x=4, y=180)
  
    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()

setup()


