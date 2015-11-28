### FIRST GUI
from tkinter import *
import time
import webbrowser
from PIL import Image, ImageTk
import winsound

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("                                                                                    "
                          "GOOD LOOKING FUNDUROS ON THE ROAD")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        edit = Menu(menu)
        edit.add_command(label="Show Img", command=self.showImg())
        edit.add_command(label="Show Text", command=self.showText(time))
        blackButton = Button(self, text="BLACK FUNDURO",command=self.goto_webblack)
        blackButton.place(x=15, y=200)
        redButton = Button(self, text="RED FUNDURO",command=self.goto_webred)
        redButton.place(x=700, y=200)
        exitButton = Button(self, text="CLICK TO EXIT",command=self.client_exit)
        exitButton.place(x=350, y=450)
    def  showImg(self):
        load = Image.open("untitled.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
    def showText(self,time):
        self.time = time.sleep(0.1)
        self.sound1()
        text = Label(self, text="""
        WHICH ONE DO YOU LIKE MORE, THE BLACK ONE OR THE RED ONE ???
        """)
        text.pack()
    def goto_webblack(self):
        url = 'https://www.facebook.com/davor.svilar'
        webbrowser.open_new_tab(url)
        self.sound2()
    def goto_webred(self):
        url = 'https://www.facebook.com/pavle.bektasevic'
        webbrowser.open_new_tab(url)
        self.sound2()
    def sound1(self):
        winsound.PlaySound("tada.wav", winsound.SND_ALIAS)
    def sound2(self):
        winsound.PlaySound("intro.wav", winsound.SND_ALIAS)
    def client_exit(self):
        self.sound1()
        exit()
root = Tk()
root.geometry("800x483")
app = Window(root)
root.mainloop()