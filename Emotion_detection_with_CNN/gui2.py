from tkinter import *
from tkinter import filedialog
import os


root =Tk()
root.title('Live_Emotion_detection')
root.iconbitmap("C:\\Users\\Rohit\\OneDrive\\Desktop\\Project\\Emotion_detection_with_CNN\\nitr_logo.ico")
root.geometry("720x480")

def submit():
    # my_program = filedialog.askopenfilename()
    # my_label.config(text=my_program)
    # #Open the program
    # os.system('"%s"' % my_program)
    
    code="C:\\Users\\Rohit\\OneDrive\\Desktop\\Project\\Emotion_detection_with_CNN\\TestEmotionDetector.py"
    os.system('"%s"' % code)

def submit1():
    # my_program = filedialog.askopenfilename()
    # my_label.config(text=my_program)
    # #Open the program
    # os.system('"%s"' % my_program)
    
    code="C:\\Users\\Rohit\\OneDrive\\Desktop\\Project\\Emotion_detection_with_CNN\\TestEmotionDetector1.py"
    os.system('"%s"' % code)

my_button =Button(root, text="Run Video", command=submit)
 
my_button.pack(pady=100,padx=100)
# my_button2 =Button(root, text="Submit", command=submit)



my_button2 =Button(root, text="Use Camera", command=submit1) 
my_button2.pack(pady=100,padx=100)
# my_button2 =Button(root, text="Submit", command=submit)


my_label = Label(root, text="")
my_label.pack(pady=100,padx=100)

root.mainloop()