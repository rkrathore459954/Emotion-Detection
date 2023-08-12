from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
import TestEmotionDetector_video
import tkinter as tk
from PIL import Image, ImageTk


root = Tk()
root.title('Live_Emotion_detection')
root.iconbitmap("C:\\Users\\Rohit\\OneDrive\\Desktop\\Project\\Emotion_detection_with_CNN\\nitr_logo.ico")
root.geometry("680x364")
root.resizable(False,False)

bg_image = PhotoImage(file="C:\\Users\\Rohit\\OneDrive\\Desktop\\Project\\Emotion_detection_with_CNN\\g\\ABBCDE1.png")
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)



style = ttk.Style()
style.configure('Rounded.TButton', foreground='Blue', font=('Arial', 12), background='#5FCBEF', relief='flat', borderwidth=0, bordercolor='#5FCBEF', focuscolor='Blue')


# my_text=Label(root,image=bg,text="LIVE EMOTION DETECTIOIN!",font=("Helvetica",20))
# my_text.pack(pady=30)

def submit():
    # my_program = filedialog.askopenfilename()
    # my_label.config(text=my_program)
    # #Open the program
    # os.system('"%s"' % my_program)

    
    
    file_path = filedialog.askopenfilename()
    final_path= os.path.join("C:\\Users\\Rohit\\OneDrive\\Desktop\\Project\\Emotion_detection_with_CNN\\video\\", file_path)
    if file_path:
        TestEmotionDetector_video.video_upload(file_path)
    os.system('"%s"' % code)


def submit1():
    # my_program = filedialog.askopenfilename()
    # my_label.config(text=my_program)
    # #Open the program
    # os.system('"%s"' % my_program)
    
    code="C:\\Users\\Rohit\\OneDrive\\Desktop\\Project\\Emotion_detection_with_CNN\\TestEmotionDetector1.py"
    os.system('"%s"' % code)

def submit_noemogi():
    code="C:\\Users\\Rohit\\OneDrive\\Desktop\\Project\\Emotion_detection_with_CNN\\TestEmotionDetector.py"
    os.system('"%s"' % code)

def submit_noemogi2():
    code="C:\\Users\\Rohit\\OneDrive\\Desktop\\Project\\Emotion_detection_with_CNN\\Test2.py"
    os.system('"%s"' % code)

def submit_noemogi3():
    code="C:\\Users\\Rohit\\OneDrive\\Desktop\\Project\\Emotion_detection_with_CNN\\test_no_upload.py"
    os.system('"%s"' % code)

my_button_noemo =ttk.Button(root,text="Text Video", command=submit_noemogi, style='Rounded.TButton') 
my_button_noemo.place(x=520,y=40)

my_button_liv =ttk.Button(root, text="Text live", command=submit_noemogi2, style='Rounded.TButton')  
my_button_liv.place(x=520,y=100)


my_button =ttk.Button(root, text="Upload video", command=submit, style='Rounded.TButton')  
my_button.place(x=520,y=280)

my_button2_v =ttk.Button(root,text="Emoji video", command=submit_noemogi3, style='Rounded.TButton') 
my_button2_v.place(x=520,y=160)



my_button2 =ttk.Button(root,text="Emoji Live", command=submit1, style='Rounded.TButton') 
my_button2.place(x=520,y=220)


button_exit=ttk.Button(root,text="Exit Programme",command=root.quit, style='Rounded.TButton')
button_exit.place(x=280,y=300)


my_label = Label(root, text="")
# my_label.pack(pady=100, padx=100)

root.mainloop()