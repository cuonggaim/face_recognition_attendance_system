from tkinter import *
from tkinter import ttk
from turtle import title
from PIL import Image, ImageTk

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("Hệ thống nhận dạng khuôn mặt")
      
      
        #1st img
        img = Image.open(r"H:\Face_Recognition_System\college_images\face-recognition.png")
        img = img.resize((400,100),Image.ANTIALIAS)
        self.photoing = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image = self.photoing)
        f_lbl.place(x=0,y=0,width=400, height=100)
        
        
        #2nd img
        img1 = Image.open(r"H:\Face_Recognition_System\college_images\smart-attendance.jpg")
        img1 = img1.resize((400,100),Image.ANTIALIAS)
        self.photoing1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image = self.photoing1)
        f_lbl.place(x=400,y=0,width=400, height=100)
        
        
        #3rd img
        img2 = Image.open(r"H:\Face_Recognition_System\college_images\iStock-182059956_18390_t12.jpg")
        img2 = img2.resize((400,100),Image.ANTIALIAS)
        self.photoing2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image = self.photoing2)
        f_lbl.place(x=800,y=0,width=400, height=100)
        
        
        #bg img
        img3 = Image.open(r"H:\Face_Recognition_System\college_images\bgimg.jpg")
        img3 = img3.resize((1200,600),Image.ANTIALIAS)
        self.photoing3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image = self.photoing3)
        bg_img.place(x=0,y=100,width=1200, height=500)
        
        title_lbl = Label(bg_img, text = "HỆ THỐNG ĐIỂM DANH NHẬN DẠNG KHUÔN MẶT", font=("times new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1200, height=45)
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()