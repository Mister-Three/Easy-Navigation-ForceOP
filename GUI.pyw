import webbrowser
import time 
import pyfiglet
import os
from tkinter import *
cope = [
    'https://minecraftforceop.com/forums',
    'https://minecraftforceop.com',
    'https://minecraftforceop.com/forums/wiki',
    'https://minecraftforceop.com/forums/downloads/',
    'https://minecraftforceop.com/forums/forums/2',
    'https://minecraftforceop.com/forums/forums/7/',
    'https://minecraftforceop.com/forums/forums/30/',
    'https://minecraftforceop.com/forums/forums/31/',
    'https://minecraftforceop.com/forums/forums/21/',
    'https://minecraftforceop.com/forums/forums/20/',
    'https://minecraftforceop.com/forums/forums/19/',
    'https://minecraftforceop.com/forums/forums/28/',
    'https://minecraftforceop.com/forums/forums/29/',
    'https://minecraftforceop.com/forums/forums/6/',
    'https://minecraftforceop.com/forums/forums/12/',
    'https://minecraftforceop.com/forums/forums/17/'
]
def forumsopen():
    URL = cope[0]
    webbrowser.open(URL)
def forceopopen():
    URL = cope[1]
    webbrowser.open(URL)
def wikiopen():
    URL = cope[2]
    webbrowser.open(URL)
def downloadsopen():
    URL = cope[3]
    webbrowser.open(URL)
def changelogopen():
    URL = cope[4]
    webbrowser.open(URL)
def bugreportsopen():
    URL = cope[5]
    webbrowser.open(URL)
def serversopen():
    URL = cope[6]
    webbrowser.open(URL)
def requestsopen():
    URL = cope[7]
    webbrowser.open(URL)
def DandGopen():
    URL = cope[8]
    webbrowser.open(URL)
def CandGopen():
    URL = cope[9]
    webbrowser.open(URL)
def videosopen():
    URL = cope[10]
    webbrowser.open(URL)
def servicesopen():
    URL = cope[11]
    webbrowser.open(URL)
def productsopen():
    URL = cope[12]
    webbrowser.open(URL)
def installingopen():
    URL = cope[13]
    webbrowser.open(URL)
def codingopen():
    URL = cope[14]
    webbrowser.open(URL)
def OTandGopen():
    URL = cope[15]
    webbrowser.open(URL)

class App:
    def __init__(self, master):


        frame = Frame(master)
        frame.pack()
        frame.configure(background="#000000")

        self.button = Button(frame, text="Exit", bg="#FF0040", fg="#ffffff", font="none 18", command=quit)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Wiki", bg="#F4A201", fg="#ffffff", font="none 18", command=wikiopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Server", bg="#F4A201", fg="#ffffff", font="none 18", command=serversopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Videos", bg="#fe50d4", fg="#ffffff", font="none 18", command=videosopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Coding", bg="#80bed4", fg="#ffffff", font="none 18", command=codingopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Forums", bg="#f3ea4e", fg="#ffffff", font="none 18", command=forumsopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Services", bg="#fe0601", fg="#ffffff", font="none 18", command=servicesopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="ForceOP", bg="#fe6501", fg="#ffffff", font="none 18", command=forceopopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Products", bg="#FFD700", fg="#ffffff", font="none 18", command=productsopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Installing", bg="#01ea4e", fg="#ffffff", font="none 18", command=installingopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Requests", bg="#c1ea4e", fg="#ffffff", font="none 18", command=requestsopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Changelog", bg="#000000", fg="#ffffff", font="none 18", command=changelogopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Downloads", bg="#fffdff", fg="#000000", font="none 18", command=downloadsopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Bug Report", bg="#00b100", fg="#ffffff", font="none 18", command=bugreportsopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Discussion & Games", bg="#d9b100", fg="#ffffff", font="none 18", command=DandGopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Contests & Giveaways", bg="#d9b100", fg="#ffffff", font="none 18", command=CandGopen)
        self.button.pack(side=BOTTOM)

        self.button = Button(frame, text="Other Tutorials/guides", bg="#d97000", fg="#ffffff", font="none 18", command=OTandGopen)
        self.button.pack(side=BOTTOM)


root = Tk()
root.title("Easy Navigation")
root.configure(background="#357000")
root.geometry('580x880')

app = App(root)
Label(root, text="Easy Navigation To ForceOP", bg="#03abd3", fg="#ffffff", font="none 18").pack()

root.mainloop()