import tkinter as tk
from tkinter import *
import tkinter.font as font
import speech_recognition as sr
import os
import subprocess
from subprocess import PIPE, Popen
#==================================================
root=tk.Tk()
root.title("speech to text")
root.geometry("300x450+300+200")
root.resizable(width=False, height=False)
def speech():
    r = sr.Recognizer()
    r2=sr.Recognizer()
    r3=sr.Recognizer()
    r4=sr.Recognizer()
    
    with sr.Microphone() as source:
        #print("Speak Anything :")
        audio = r.listen(source)
        try:
            text_1 = r.recognize_google(audio)
            text.insert(tk.END,text_1+" ")
        except:
            text.insert(tk.END,"Sorry could not recognize what you said")
    
    if "save it" in r2.recognize_google(audio): 
        try:
            result = text.get(1.0,END)
            file = open('C:\\Users\\Akash\\Desktop\\geek.txt', 'a') 
            final_text=' '.join(result.split(' ')[:-3])   
            file.write(final_text+"\n")
            file.close()
        except:
            print("sorry")
            
    if "clear it" in r3.recognize_google(audio):
        text.delete('1.0', END)
        
    if 'open file' in r4.recognize_google(audio):
        subprocess.call(['notepad.exe', 'C:\\Users\\Akash\\Desktop\\geek.txt'])
#===========================================================           
text=tk.Text(root,width=30,height=10,padx=10,bd=5,wrap=WORD)
text.pack(side=TOP, anchor=W, fill=Y, expand=YES)
#===========================================================
myFont = font.Font(family='Helvetica')
button=tk.Button(root,text="press one time and speak...",command=lambda:speech())
button['font'] = myFont
button.pack(side=BOTTOM,anchor=W, fill=X)


root.mainloop()