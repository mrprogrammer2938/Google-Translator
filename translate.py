#!/usr/bin/python3
# Google Translator v1.4.2
try:
    from tkinter import *
except ImportError:
    os.system("pip install tkinter")
try:
    from colorama import Fore,init
except ImportError:
    os.system("pip install colorama")
try:
    from deep_translator import GoogleTranslator
except ImportError:
    os.system("pip install deep_translator")
import os
import platform
import datetime
init()
system = platform.system()
root = Tk()
End = '\033[0m'
banner = """{}
MMMMMMMMMMMMWNXK000OO00KKXNWMMMMMMMMMMMM
MMMMMMMMWNKOxdllcccccccclldxOKNWMMMMMMMM
MMMMMMWKkolccccccccccccccccccldONMMMMMMM
MMMMWKxlcccccccccccccccccccccld0NMMMMMMM
MMMNOocccccccloxkO0000OkxolldONWMMMMMMMM
MMNOlccccccokKNWMMMMMMMMWNK0NWMMMMMMMMMM
MWKOxolcclxKWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MN0OOOkdokNWMMMMMMMWWWWWNNNNNNNNNWNWWWMM
WXOOOOOO0NMMMMMMMMWKxxdddddddddddddddONM
WKOOOOOOKWMMMMMMMMWOoolllllllllllllllxXM
WKOOOOOOKWMMMMMMMMWOoolllllllllllllllxXM
WX0OOOOkkKWMMMMMMMWXOOkkOOkOkkollllllkNM
MNKOOkdoldKWMMMMMMMMMMMMMMMMW0dlllllo0WM
MMXkdlllllokXWMMMMMMMMMMMMWNOdllllloONMM
MMWKdlllllllox0KNNWWWWNNX0kdllllllokNMMM
MMMWXkolllllllllodxxxxdoolllllllld0NMMMM
MMMMMWKkolllllllllllllllllllllldOXWMMMMM
MMMMMMMWX0kdlllllllllllllllldk0NWMMMMMMM
MMMMMMMMMMWNK0OkxxddddxxkO0KNWMMMMMMMMMM
MMMMMMMMMMMMMMMWWNNNNNNWWMMMMMMMMMMMMMMM{}\n""".format(Fore.GREEN,End)
root.title("Google Translate")
welcome = Label(root,text="Google Translate",bg="white",fg="blue").pack()
word = Entry(root,width="30",bg="cyan")
word.pack()
word.place(bordermode=OUTSIDE,x=85,y=50)
word.get()
sour = Entry(root,width=9)
sour.pack()
sour.place(bordermode=OUTSIDE,x=150,y=70)
sour.insert(0,"Source")
sour.get()
target_ = Entry(root,width=9)
target_.pack()
target_.place(bordermode=OUTSIDE,x=150,y=90)
target_.insert(0,"Target")
target_.get()
def cls():
    if system == 'Linux':
        os.system("clear")
    else:
        os.system("cls")
def reset_():
    word.delete(0,END)
    sour.delete(0,END)
    target_.delete(0,END)
def exit_translate():
    root.destroy()
    cls()
def start_translate():
    run = GoogleTranslator(source=sour.get(),target=target_.get()).translate(word.get())
    txt = Label(root,text=run,fg="black",bg="white")
    txt.pack()
    txt.place(bordermode=OUTSIDE,x=145,y=115)
    reset = Button(root,text="Reset",fg="green",bg="white",command=reset_,width=9,height=3)
    reset.pack()
    reset.place(bordermode=OUTSIDE,x=145,y=220)
cls()
start = Button(root,text="Translate",fg="green",bg="white",command=start_translate,width=13,height=3)
start.pack()
start.place(bordermode=OUTSIDE,x=133,y=160)
exit = Button(root,text="Exit",fg="green",bg="white",command=exit_translate,width=9,height=3)
exit.pack()
exit.place(bordermode=OUTSIDE,x=145,y=280)
photo = PhotoImage(file="google-logo-3.png")
root.configure(background="white")
root.iconphoto(False,photo)
root.resizable(True,True)
root.geometry("350x350")
time_ = datetime.datetime.now()
print(banner)
print("Start Google Translate At: {}".format(time_))

root.mainloop()
