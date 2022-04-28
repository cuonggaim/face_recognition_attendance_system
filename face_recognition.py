from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+0+0")
        self.root.title("Hệ thống nhận dạng khuôn mặt")
        
        title_lbl = Label(self.root, text = "NHẬN DẠNG KHUÔN MẶT", font=("times new roman", 25, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1200, height=60)
        
        img_left = Image.open(r"college_images\face_detector1.jpg")
        img_left = img_left.resize((600,480),Image.ANTIALIAS)
        self.photoing_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(self.root, image = self.photoing_left)
        f_lbl.place(x=0,y=60,width=600, height=480)
        
        
        img_right = Image.open(r"college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_right = img_right.resize((600,480),Image.ANTIALIAS)
        self.photoing_right = ImageTk.PhotoImage(img_right)
        
        f_lbl = Label(self.root, image = self.photoing_right)
        f_lbl.place(x=600,y=60,width=600, height=480)
        
        
        b1_1 = Button(f_lbl, text = "Nhận dạng khuôn mặt", cursor = "hand2", font=("times new roman", 12, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=218, y = 425, width = 155, height = 25)
        
        
    #face recognition------------------------
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            
            coord = []
            
            for (x, y, w, h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select name from student where studentID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select class from student where studentID="+str(id))
                c=my_cursor.fetchone()
                c="+".join(c)
                
                my_cursor.execute("select dep from student where studentID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                if confidence>77:
                    cv2.putText(img,f"Lớp:{c}",(x,y-55), cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Họ và tên:{n}",(x,y-30), cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Chuyên ngành:{d}",(x,y-5), cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Khuôn mặt không xác định",(x,y-5), cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,y]
        
            return coord
        
        def recognize(img, clf, faceCascade):
            coord=draw_boundray(img, faceCascade, 1.1, 10, (255,25,255), "Khuôn mặt", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Chào mừng bạn",img)
            
            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
  
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()