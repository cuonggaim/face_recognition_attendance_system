from tkinter import *
from tkinter import ttk
from turtle import title
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("Hệ thống nhận dạng khuôn mặt")
        
        
        title_lbl = Label(self.root, text = "DEVELOPER", font=("times new roman", 25, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1200, height=60)
        
        
        img_top = Image.open(r"college_images\dev.jpg")
        img_top = img_top.resize((1200,540),Image.ANTIALIAS)
        self.photoing_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image = self.photoing_top)
        f_lbl.place(x=0,y=60,width=1200, height=540)
        
        
        main_frame = Frame(f_lbl, bd= 2, bg="white")
        main_frame.place(x=670, y=20, width=500, height= 500)
        
        img_me = Image.open(r"college_images\cuong.jpg")
        img_me = img_me.resize((200,200),Image.ANTIALIAS)
        self.photoing_me = ImageTk.PhotoImage(img_me)
        
        f_lbl = Label(main_frame, image = self.photoing_me)
        f_lbl.place(x=300,y=-5,width=200, height=200)
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()