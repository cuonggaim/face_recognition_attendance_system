from tkinter import *
from tkinter import ttk
from turtle import title
from PIL import Image, ImageTk
from student import Student
import os
from train import Train

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("Hệ thống nhận dạng khuôn mặt")
        
        
        #1st img
        img = Image.open(r"college_images\DHV1.jpg")
        img = img.resize((400,100),Image.ANTIALIAS)
        self.photoing = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image = self.photoing)
        f_lbl.place(x=0,y=0,width=400, height=100)
        
        
        #2nd img
        img1 = Image.open(r"college_images\facialrecognition.png")
        img1 = img1.resize((400,100),Image.ANTIALIAS)
        self.photoing1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image = self.photoing1)
        f_lbl.place(x=400,y=0,width=400, height=100)
        
        
        #3rd img
        img2 = Image.open(r"college_images\DHV2.jpg")
        img2 = img2.resize((400,100),Image.ANTIALIAS)
        self.photoing2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image = self.photoing2)
        f_lbl.place(x=800,y=0,width=400, height=100)
        
        
        #bg img
        img3 = Image.open(r"college_images\bgimg.jpg")
        img3 = img3.resize((1200,600),Image.ANTIALIAS)
        self.photoing3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image = self.photoing3)
        bg_img.place(x=0,y=100,width=1200, height=500)
        
        title_lbl = Label(bg_img, text = "HỆ THỐNG ĐIỂM DANH NHẬN DẠNG KHUÔN MẶT", font=("times new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1200, height=45)
        
        
        #stu button
        img4 = Image.open(r"college_images\student.jpg")
        img4 = img4.resize((150,150),Image.ANTIALIAS)
        self.photoing4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(bg_img, image = self.photoing4, command=self.student_details, cursor = "hand2")
        b1.place(x=120, y = 100, width = 150, height = 150)
        
        b1_1 = Button(bg_img, text = "Student Details", command=self.student_details, cursor = "hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=120, y = 210, width = 150, height = 40)
        
        
        #detection button
        img5 = Image.open(r"college_images\face_detector1.jpg")
        img5 = img5.resize((150,150),Image.ANTIALIAS)
        self.photoing5 = ImageTk.PhotoImage(img5)
        
        b1 = Button(bg_img, image = self.photoing5, cursor = "hand2")
        b1.place(x=390, y = 100, width = 150, height = 150)
        
        b1_1 = Button(bg_img, text = "Face Detection", cursor = "hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=390, y = 210, width = 150, height = 40)
        
        
        #attendance button
        img6 = Image.open(r"college_images\report.jpg")
        img6 = img6.resize((150,150),Image.ANTIALIAS)
        self.photoing6 = ImageTk.PhotoImage(img6)
        
        b1 = Button(bg_img, image = self.photoing6, cursor = "hand2")
        b1.place(x=660, y = 100, width = 150, height = 150)
        
        b1_1 = Button(bg_img, text = "Attendance", cursor = "hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=660, y = 210, width = 150, height = 40)
        
        
        #help button
        img7 = Image.open(r"college_images\help-desk.jpg")
        img7 = img7.resize((150,150),Image.ANTIALIAS)
        self.photoing7 = ImageTk.PhotoImage(img7)
        
        b1 = Button(bg_img, image = self.photoing7, cursor = "hand2")
        b1.place(x=950, y = 100, width = 150, height = 150)
        
        b1_1 = Button(bg_img, text = "Help Desk", cursor = "hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=950, y = 210, width = 150, height = 40)
        
        
        #train face button
        img8 = Image.open(r"college_images\Train.jpg")
        img8 = img8.resize((150,150),Image.ANTIALIAS)
        self.photoing8 = ImageTk.PhotoImage(img8)
        
        b1 = Button(bg_img, image = self.photoing8, cursor = "hand2", command= self.train_data)
        b1.place(x=120, y = 300, width = 150, height = 150)
        
        b1_1 = Button(bg_img, text = "Train Data", cursor = "hand2", command= self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=120, y = 410, width = 150, height = 40)
        
        
        #photos face button
        img9 = Image.open(r"college_images\photo-face.png")
        img9 = img9.resize((150,150),Image.ANTIALIAS)
        self.photoing9 = ImageTk.PhotoImage(img9)
        
        b1 = Button(bg_img, image = self.photoing9, cursor = "hand2", command=self.open_img)
        b1.place(x=390, y = 300, width = 150, height = 150)
        
        b1_1 = Button(bg_img, text = "Photos", cursor = "hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=390, y = 410, width = 150, height = 40)
        
        
        #Developer button
        img10 = Image.open(r"college_images\Team-Management-Software-Development.jpg")
        img10 = img10.resize((150,150),Image.ANTIALIAS)
        self.photoing10 = ImageTk.PhotoImage(img10)
        
        b1 = Button(bg_img, image = self.photoing10, cursor = "hand2")
        b1.place(x=660, y = 300, width = 150, height = 150)
        
        b1_1 = Button(bg_img, text = "Developer", cursor = "hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=660, y = 410, width = 150, height = 40)
        
        
        #exit button
        img11 = Image.open(r"college_images\exit.jpg")
        img11 = img11.resize((150,150),Image.ANTIALIAS)
        self.photoing11 = ImageTk.PhotoImage(img11)
        
        b1 = Button(bg_img, image = self.photoing11, cursor = "hand2")
        b1.place(x=950, y = 300, width = 150, height = 150)
        
        b1_1 = Button(bg_img, text = "Exit", cursor = "hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=950, y = 410, width = 150, height = 40)
        
        
    
    def open_img(self):
        os.startfile("data")
        
        
        
        
    #Function button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()