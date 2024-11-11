from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="blue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        
        
        #Frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)
        
        img_top1 = Image.open(r"E:\ing\download (5).jpeg")
        img_top1 = img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        
        f_lbl = Label(main_frame, image=self.photoimg_top)
        f_lbl.place(x=300, y=0, width=200, height=200)
        
        # Devloper info
        dep_label = Label(main_frame, text="hello my is", font=("times new roman", 20,"bold"),bg="white")
        dep_label.place(x=0,y=5)
        
        dep_label = Label(main_frame, text=" i am full stackdeveloper", font=("times new roman", 20,"bold"),bg="white")
        dep_label.place(x=0,y=40)
        
        img2 = Image.open(r"E:\ing\iStock-classroom-girls-students-school.jpg")
        img2 = img2.resize((500, 390))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=210, width=500, height=300)
        
        
        
        
        
    if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()  
    
    
    
    #help desk
    from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="blue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        
        
        #Frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)
        
        img_top1 = Image.open(r"E:\ing\download (5).jpeg")
        img_top1 = img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)
        
        dep_label = Label(f_lbl, text="Email:official11@gmail.com", font=("times new roman", 20,"bold"),bg="white")
        dep_label.place(x=0,y=5)
        
        
        
        
        
    if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()  
    