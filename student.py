from tkinter import *
from tkinter import ttk
from turtle import title
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("Hệ thống nhận dạng khuôn mặt")
        
        
        #Variables---------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_class=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
      
      
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
        
        title_lbl = Label(bg_img, text = "HỆ THỐNG QUẢN LÝ SINH VIÊN", font=("times new roman", 25, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1200, height=45)
        
        
        main_frame = Frame(bg_img, bd= 2, bg="white")
        main_frame.place(x=25, y=50, width=1150, height= 440)
        
        
        #left label frame
        Left_frame = LabelFrame(main_frame, bd= 2, bg="white", relief= RIDGE, text="Chi Tiết Sinh Viên", font= ("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=5, width= 550, height= 420)
        
        img_left = Image.open(r"H:\Face_Recognition_System\college_images\iStock-182059956_18390_t12.jpg")
        img_left = img_left.resize((535,100),Image.ANTIALIAS)
        self.photoing_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame, image = self.photoing_left)
        f_lbl.place(x=5,y=0,width=535, height=100)
        
        #Current course
        current_course_frame = LabelFrame(Left_frame, bd= 2, bg="white", relief= RIDGE, text="Thông tin khóa học hiện tại", font= ("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=100, width= 535, height= 80)
        
        #Department
        dep_label = Label(current_course_frame, text = "Chuyên ngành:", font= ("times new roman", 11, "bold"), bg="white")
        dep_label.grid( row = 0, column = 0, padx=2, sticky=W)
        
        dep_combo = ttk.Combobox( current_course_frame, textvariable=self.var_dep, font= ("times new roman", 10), state = "readonly", width = 35)
        dep_combo["values"] = ("Chọn chuyên ngành", "Kỹ thuật Điện tử, Viễn thông", "Kỹ thuật Điều khiển và Tự động hóa",
                               "Công nghệ Kỹ thuật Điện, Điện tử", "Công nghệ thông tin",
                               "Công nghệ Kỹ thuật ô tô", "Công nghệ Kỹ thuật Nhiệt, Điện lạnh",
                               "Kỹ thuật phần mềm")
        dep_combo.current(0)
        dep_combo.grid( row = 0, column = 1, padx=2, pady=4)
        
        #course
        course_label = Label(current_course_frame, text = "Khóa:", font= ("times new roman", 11, "bold"), bg="white")
        course_label.grid( row = 0, column = 2, padx=2, sticky=W)
        
        course_combo = ttk.Combobox( current_course_frame, textvariable=self.var_course, font= ("times new roman", 10), state = "readonly", width = 14)
        course_combo["values"] = ("Chọn khóa", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64")
        course_combo.current(0)
        course_combo.grid( row = 0, column = 3, padx=2, pady=4)
        
        #semester
        semester_label = Label(current_course_frame, text = "Học kỳ:", font= ("times new roman", 11, "bold"), bg="white")
        semester_label.grid( row = 1, column = 0, padx=2, sticky=W)
        
        semester_combo = ttk.Combobox( current_course_frame, textvariable=self.var_semester, font= ("times new roman", 10), state = "readonly", width = 35)
        semester_combo["values"] = ("Chọn học kỳ", "Học kỳ 1", "Học kỳ 2", "Học kỳ hè")
        semester_combo.current(0)
        semester_combo.grid( row = 1, column = 1, padx=2, pady=4)
        
        #year
        year_label = Label(current_course_frame, text = "Năm học:", font= ("times new roman", 11, "bold"), bg="white")
        year_label.grid( row = 1, column = 2, padx=2, sticky=W)
        
        year_combo = ttk.Combobox( current_course_frame, textvariable=self.var_year, font= ("times new roman", 10), state = "readonly", width = 14)
        year_combo["values"] = ("Chọn năm học", "2016-2017", "2017-2018", "2018-2019", "2019-2020", "2020-2021", "2021-2022", "2022-2023", "2023-2024", "2024-2025")
        year_combo.current(0)
        year_combo.grid( row = 1, column = 3, padx=2, pady=4)
        
        #class student information
        class_student_frame = LabelFrame(Left_frame, bd= 2, bg="white", relief= RIDGE, text="Thông tin sinh viên", font= ("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=180, width= 535, height= 210)
        
        #studentId
        studentId_label = Label(class_student_frame, text = "Mã số sinh viên: ", font= ("times new roman", 11, "bold"), bg="white")
        studentId_label.grid( row = 0, column = 0, padx=2, pady=4, sticky=W)
        
        studentId_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width = 20, font= ("times new roman", 11))
        studentId_entry.grid( row = 0, column = 1, padx=2, pady=4, sticky=W)
        
        #studentName
        studentName_label = Label(class_student_frame, text = "Họ và tên: ", font= ("times new roman", 11, "bold"), bg="white")
        studentName_label.grid( row = 0, column = 2, padx=2, pady=4, sticky=W)
        
        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width = 20, font= ("times new roman", 11))
        studentName_entry.grid( row = 0, column = 3, padx=2, pady=4, sticky=W)
        
        #class
        class_label = Label(class_student_frame, text = "Lớp: ", font= ("times new roman", 11, "bold"), bg="white")
        class_label.grid( row = 1, column = 0, padx=2, pady=4, sticky=W)
        
        class_entry = ttk.Entry(class_student_frame, textvariable=self.var_class, width = 20, font= ("times new roman", 11))
        class_entry.grid( row = 1, column = 1, padx=2, pady=4, sticky=W)
        
        #gender
        gender_label = Label(class_student_frame, text = "Giới tính: ", font= ("times new roman", 11, "bold"), bg="white")
        gender_label.grid( row = 1, column = 2, padx=2, pady=4, sticky=W)
        
        gender_combo = ttk.Combobox( class_student_frame, textvariable=self.var_gender, font= ("times new roman", 10), state = "readonly", width = 20)
        gender_combo["values"] = ("Chọn giới tính", "Nam", "Nữ", "Khác")
        gender_combo.current(0)
        gender_combo.grid( row = 1, column = 3, padx=2, pady=4, sticky=W)
        
        #date of birth
        dob_label = Label(class_student_frame, text = "Ngày sinh: ", font= ("times new roman", 11, "bold"), bg="white")
        dob_label.grid( row = 2, column = 0, padx=2, pady=4, sticky=W)
        
        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width = 20, font= ("times new roman", 11))
        dob_entry.grid( row = 2, column = 1, padx=2, pady=4, sticky=W)
        
        #email
        email_label = Label(class_student_frame, text = "Email: ", font= ("times new roman", 11, "bold"), bg="white")
        email_label.grid( row = 2, column = 2, padx=2, pady=4, sticky=W)
        
        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width = 20, font= ("times new roman", 11))
        email_entry.grid( row = 2, column = 3, padx=2, pady=4, sticky=W)
        
        #phoneNumber
        phoneNumber_label = Label(class_student_frame, text = "Số điện thoại: ", font= ("times new roman", 11, "bold"), bg="white")
        phoneNumber_label.grid( row = 3, column = 0, padx=2, pady=4, sticky=W)
        
        phoneNumber_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width = 20, font= ("times new roman", 11))
        phoneNumber_entry.grid( row = 3, column = 1, padx=2, pady=4, sticky=W)
        
        #address
        address_label = Label(class_student_frame, text = "Địa chỉ: ", font= ("times new roman", 11, "bold"), bg="white")
        address_label.grid( row = 3, column = 2, padx=2, pady=4, sticky=W)
        
        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width = 20, font= ("times new roman", 11))
        address_entry.grid( row = 3, column = 3, padx=2, pady=4, sticky=W)
        
        #radio button
        self.var_radio1 = StringVar()
        radioButton1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Có ảnh", value="Yes")
        radioButton1.grid( row = 6, column = 0)
        
        radioButton2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Không có ảnh", value="No")
        radioButton2.grid( row = 6, column = 1)
        
        #button frame
        btn_frame = Frame(class_student_frame, bd = 2, relief= RIDGE, bg="white")
        btn_frame.place(x=0, y= 155, width="530", height="30")
        
        #button save
        save_btn = Button(btn_frame, text="Lưu", command=self.add_data, width="8", font= ("times new roman", 11, "bold"), bg="blue", fg="white")
        save_btn.grid(row = 0, column = 0, padx=4)
        
        #button update
        update_btn = Button(btn_frame, text="Sửa", command=self.update_data, width="8", font= ("times new roman", 11, "bold"), bg="blue", fg="white")
        update_btn.grid(row = 0, column = 1, padx=2)
        
        #button delete
        delete_btn = Button(btn_frame, text="Xóa", command=self.delete_data, width="8", font= ("times new roman", 11, "bold"), bg="blue", fg="white")
        delete_btn.grid(row = 0, column = 2, padx = 2)
        
        #button reset
        reset_btn = Button(btn_frame, text="Làm mới", command=self.reset_data, width="8", font= ("times new roman", 11, "bold"), bg="blue", fg="white")
        reset_btn.grid(row = 0, column = 3, padx=2)
        
        #button save photo
        take_photo_btn = Button(btn_frame, command=self.generate_dataset, text="Thêm ảnh",width="8", font= ("times new roman", 11, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row = 0, column = 4, padx=2)
        
        #button update photo
        update_photo_btn = Button(btn_frame, text="Sửa ảnh",width="8", font= ("times new roman", 11, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row = 0, column = 5, padx=4)
        
        
        #right label frame
        Right_frame = LabelFrame(main_frame, bd= 2, bg="white", relief= RIDGE, text="Chi Tiết Sinh Viên", font= ("times new roman", 12, "bold"))
        Right_frame.place(x=585, y=5, width= 550, height= 420)
        
        img_right = Image.open(r"H:\Face_Recognition_System\college_images\student.jpg")
        img_right = img_right.resize((535,100),Image.ANTIALIAS)
        self.photoing_right = ImageTk.PhotoImage(img_right)
        
        f_lbl = Label(Right_frame, image = self.photoing_right)
        f_lbl.place(x=5,y=0,width=535, height=100)
        
        #search frame
        search_frame = LabelFrame(Right_frame, bd= 2, bg="white", relief= RIDGE, text="Tìm kiếm", font= ("times new roman", 12, "bold"))
        search_frame.place(x=5, y=100, width= 535, height= 50)
        
        search_label = Label(search_frame, text = "Tìm kiếm theo: ", font= ("times new roman", 10, "bold"), bg="red", fg="white")
        search_label.grid( row = 0, column = 0, padx=5, pady=2, sticky=W)
        
        search_combo = ttk.Combobox( search_frame, font= ("times new roman", 11), state = "readonly", width = 12)
        search_combo["values"] = ("Chọn", "Chuyên ngành", "Khóa", "Học kỳ", "Năm học", "MSSV", "Họ và tên",
                                                               "Lớp", "Giới tính", "Ngày sinh", "Email", "SĐT", "Địa chỉ")
        search_combo.current(0)
        search_combo.grid( row = 0, column = 1, padx=2, pady=2, sticky=W)
        
        search_entry = ttk.Entry(search_frame, width = 18, font= ("times new roman", 11))
        search_entry.grid( row = 0, column = 2, padx=2, sticky=W)
        
        search_btn = Button(search_frame, text="Tìm kiếm",width="11", font= ("times new roman", 10, "bold"), bg="blue", fg="white")
        search_btn.grid(row = 0, column = 3, padx=1)
        
        showAll_btn = Button(search_frame, text="Hiển thị tất cả",width="11", font= ("times new roman", 10, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row = 0, column = 4, padx=1)
        
        #table frame
        table_frame = LabelFrame(Right_frame, bd= 2, bg="white", relief= RIDGE)
        table_frame.place(x=5, y=152, width= 535, height= 243)
        
        scroll_x = ttk.Scrollbar(table_frame, orient= HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient= VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "sem", "year", "id", "name",
                                                               "class", "gender", "dob", "email", "phone", "address", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack( side=BOTTOM, fill=X)
        scroll_y.pack( side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep", text="Chuyên ngành")
        self.student_table.heading("course", text="Khóa")
        self.student_table.heading("sem", text="Học kỳ")
        self.student_table.heading("year", text="Năm học")
        self.student_table.heading("id", text="Mã số sinh viên")
        self.student_table.heading("name", text="Họ và tên")
        self.student_table.heading("class", text="Lớp")
        self.student_table.heading("gender", text="Giới tính")
        self.student_table.heading("dob", text="Ngày sinh")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Số điện thoại")
        self.student_table.heading("address", text="Địa chỉ")
        self.student_table.heading("photo", text="Ảnh")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep", width=200)
        self.student_table.column("course", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=200)
        self.student_table.column("class", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=200)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=200)
        self.student_table.column("photo", width=150)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
        
    
    #function decoration----------------------------------------------------------------
    
    def add_data(self):
        if self.var_dep.get()=="Chọn chuyên ngành" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Lỗi", "Phải điền đầy đủ các trường", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_std_id.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_class.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_radio1.get(),
                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Thành công", "Sinh viên đã được thêm vào thành công", parent=self.root)
            except Exception as es:
                messagebox.showerror("Lỗi", f"Bởi vì: {str(es)}", parent=self.root)
        
    
    #fetch data------------------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data=my_cursor.fetchall()
        
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    #get cursor------------
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_semester.set(data[2])
        self.var_year.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_class.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_email.set(data[9])
        self.var_phone.set(data[10])
        self.var_address.set(data[11])
        self.var_radio1.set(data[12])
        
    #update function------------
    def update_data(self):
        if self.var_dep.get()=="Chọn chuyên ngành" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Lỗi", "Phải điền đầy đủ các trường", parent=self.root)
        else:
            try:
                Update= messagebox.askyesno("Cập nhật", "Bạn có muốn cập nhật thông tin sinh viên này hay không?", parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set dep=%s, course=%s, semester=%s, year=%s, name=%s, class=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, photoSample=%s where studentID=%s",(
                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                        self.var_class.get(),
                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Thành công", "Thông tin sinh viên cập nhật thành công", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()    
            except Exception as e:
                messagebox.showerror("Lỗi", f"Bởi vì: {str(e)}", parent=self.root)        
    
    
    #delete function------------------------
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Lỗi","Chưa chọn sinh viên", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Xóa sinh viên", "Bạn có muốn xóa sinh viên này không ?", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where studentID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Xóa sinh viên", "Xóa sinh viên thành công", parent=self.root)
            except Exception as e:
                messagebox.showerror("Lỗi", f"Bởi vì: {str(e)}", parent=self.root)    
                
                
    #reset function--------------------------------------------------------
    def reset_data(self):
        self.var_dep.set("Chọn chuyên ngành")
        self.var_course.set("Chọn khóa")
        self.var_semester.set("Chọn học kỳ")
        self.var_year.set("Chọn năm học")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_class.set("")
        self.var_gender.set("Chọn giới tính")
        self.var_dob.set("")     
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")

          
    #Generate dataset--------------------
    def generate_dataset(self):
        if self.var_dep.get()=="Chọn chuyên ngành" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Lỗi", "Phải điền đầy đủ các trường", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set dep=%s, course=%s, semester=%s, year=%s, name=%s, class=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, photoSample=%s where studentID=%s",(
                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                                            self.var_class.get(),
                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                            self.var_std_id.get()==id+1
                                                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #Load predifiend data on face from opencv-----
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbor=5
                    
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h, x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Ảnh", face)
                    
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Kết quả", "Tạo tập dữ liệu thành công")    
            except Exception as e:
                messagebox.showerror("Lỗi", f"Bởi vì: {str(e)}", parent=self.root)    
                    
                
               
        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()