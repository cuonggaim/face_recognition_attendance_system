from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("Hệ thống nhận dạng khuôn mặt")
        
        
        #variables----------------------------------------------------------------
        self.var_atten_id=StringVar()
        self.var_atten_class=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        #1st img
        img = Image.open(r"college_images\face-recognition.png")
        img = img.resize((600,100),Image.ANTIALIAS)
        self.photoing = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image = self.photoing)
        f_lbl.place(x=0,y=0,width=600, height=100)
        
        
        #2nd img
        img1 = Image.open(r"college_images\smart-attendance.jpg")
        img1 = img1.resize((600,100),Image.ANTIALIAS)
        self.photoing1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image = self.photoing1)
        f_lbl.place(x=600,y=0,width=600, height=100)    
        
        
        #bg img
        img3 = Image.open(r"college_images\bgimg.jpg")
        img3 = img3.resize((1200,500),Image.ANTIALIAS)
        self.photoing3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image = self.photoing3)
        bg_img.place(x=0,y=100,width=1200, height=500)
        
        title_lbl = Label(bg_img, text = "HỆ THỐNG ĐIỂM DANH SINH VIÊN", font=("times new roman", 25, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1200, height=45)
        
        main_frame = Frame(bg_img, bd= 2, bg="white")
        main_frame.place(x=25, y=50, width=1150, height= 440)
        
        
        #left label frame
        Left_frame = LabelFrame(main_frame, bd= 2, bg="white", relief= RIDGE, text="Chi Tiết Điểm Danh Sinh Viên", font= ("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=5, width= 550, height= 420)
        
        img_left = Image.open(r"college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((535,100),Image.ANTIALIAS)
        self.photoing_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame, image = self.photoing_left)
        f_lbl.place(x=5,y=0,width=535, height=100)
        
        #class student information
        class_student_frame = LabelFrame(Left_frame, bd= 2, bg="white", relief= RIDGE, text="Thông tin sinh viên", font= ("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=100, width= 535, height= 250)
        
        #studentId
        studentId_label = Label(class_student_frame, text = "Mã số sinh viên: ", font= ("times new roman", 11, "bold"), bg="white")
        studentId_label.grid( row = 0, column = 0, padx=2, pady=4, sticky=W)
        
        studentId_entry = ttk.Entry(class_student_frame, width = 19,textvariable=self.var_atten_id, font= ("times new roman", 11))
        studentId_entry.grid( row = 0, column = 1, padx=2, pady=4, sticky=W)
        
        #class
        class_label = Label(class_student_frame, text = "Lớp: ", font= ("times new roman", 11, "bold"), bg="white")
        class_label.grid( row = 0, column = 2, padx=2, pady=4, sticky=W)
        
        class_entry = ttk.Entry(class_student_frame, width = 19,textvariable=self.var_atten_class, font= ("times new roman", 11))
        class_entry.grid( row = 0, column = 3, padx=2, pady=4, sticky=W)
        
        #studentName
        studentName_label = Label(class_student_frame, text = "Họ và tên: ", font= ("times new roman", 11, "bold"), bg="white")
        studentName_label.grid( row = 1, column = 0, padx=2, pady=4, sticky=W)
        
        studentName_entry = ttk.Entry(class_student_frame, width = 19,textvariable=self.var_atten_name, font= ("times new roman", 11))
        studentName_entry.grid( row = 1, column = 1, padx=2, pady=4, sticky=W)
        
        #department
        department_label = Label(class_student_frame, text = "Chuyên ngành: ", font= ("times new roman", 11, "bold"), bg="white")
        department_label.grid( row = 1, column = 2, padx=2, pady=4, sticky=W)
        
        department_entry = ttk.Entry(class_student_frame, width = 19,textvariable=self.var_atten_dep, font= ("times new roman", 11))
        department_entry.grid( row = 1, column = 3, padx=2, pady=4, sticky=W)
        
        #time
        time_label = Label(class_student_frame, text="Thời gian:", bg="white", font= ("times new roman", 11, "bold"))
        time_label.grid( row = 2, column = 0, padx=2, pady=4, sticky=W)
        
        atten_time = ttk.Entry(class_student_frame, width=19,textvariable=self.var_atten_time, font= ("times new roman", 11))
        atten_time.grid( row = 2, column = 1, padx=2, pady=4, sticky=W)
        
        #date
        date_label = Label(class_student_frame, text="Ngày:", bg="white", font= ("times new roman", 11, "bold"))
        date_label.grid( row = 2, column = 2, padx=2, pady=4, sticky=W)
        
        atten_date = ttk.Entry(class_student_frame, width=19,textvariable=self.var_atten_date, font= ("times new roman", 11))
        atten_date.grid( row = 2, column = 3, padx=2, pady=4, sticky=W)
        
        #atten
        atten_label = Label(class_student_frame, text="Trạng thái", bg="white", font= ("times new roman", 11, "bold"))
        atten_label.grid(row=3, column=0)
        
        self.atten_status=ttk.Combobox(class_student_frame, width=10,textvariable=self.var_atten_attendance,state="readonly", font= ("times new roman", 11, "bold"))
        self.atten_status["values"]=("Trạng thái", "Có mặt", "Vắng mặt")
        self.atten_status.grid(row=3, column=1, padx=2, pady=4, sticky=W)
        self.atten_status.current(0)
        
        #button frame
        btn_frame = Frame(class_student_frame, bd = 2, relief= RIDGE, bg="white")
        btn_frame.place(x=0, y= 155, width="530", height="30")
        
        #button save
        save_btn = Button(btn_frame, text="Nhập csv",command=self.importCsv, width="12", font= ("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row = 0, column = 0, padx=1)
        
        #button update
        update_btn = Button(btn_frame, text="Xuất csv",command=self.exportCsv, width="12", font= ("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row = 0, column = 1, padx=1)
        
        #button delete
        delete_btn = Button(btn_frame, text="Cập nhật", width="12", font= ("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row = 0, column = 2, padx = 1)
        
        #button reset
        reset_btn = Button(btn_frame, text="Làm mới",command=self.reset_data, width="12", font= ("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row = 0, column = 3, padx=1)
        
        
        #right label frame
        Right_frame = LabelFrame(main_frame, bd= 2, bg="white", relief= RIDGE, text="Chi Tiết Điểm Danh Sinh Viên", font= ("times new roman", 12, "bold"))
        Right_frame.place(x=585, y=5, width= 550, height= 420)
        
        table_frame = LabelFrame(Right_frame, bd= 2, bg="white", relief= RIDGE)
        table_frame.place(x=5, y=5, width= 535, height= 380)
        
        scroll_x = ttk.Scrollbar(table_frame, orient= HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient= VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame, column=("id", "class", "name", "department", "time", "date", "attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack( side=BOTTOM, fill=X)
        scroll_y.pack( side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id", text="MSSV")
        self.AttendanceReportTable.heading("class", text="Lớp")
        self.AttendanceReportTable.heading("name", text="Họ và tên")
        self.AttendanceReportTable.heading("department", text="Chuyên ngành")
        self.AttendanceReportTable.heading("time", text="Thời gian")
        self.AttendanceReportTable.heading("date", text="Ngày tháng")
        self.AttendanceReportTable.heading("attendance", text="Trạng thái")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("class", width=100)
        self.AttendanceReportTable.column("name", width=200)
        self.AttendanceReportTable.column("department", width=200)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
        
        
    #fetch data--------------------
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
         
         
    #import csv------------------------------------------------   
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd, title="Import CSV", filetypes=(("CSV File","*.csv"),("ALL File","*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
        
        
    #export csv--------------------
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Rỗng","Không có dữ liệu",parent=self.root)    
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd, title="Import CSV", filetypes=(("CSV File","*.csv"),("ALL File","*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write=csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Xuất dữ liệu", "Bạn đã xuất dữ liệu ra "+os.path.basename(fln)+" thành công")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Bởi vì: {str(e)}", parent=self.root)
            
            
    def get_cursor(self, event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_class.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
        
    def reset_data(self, event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set("")
        self.var_atten_class.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()