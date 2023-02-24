from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")
root.geometry("750x250")
def time():
    string= strftime("%I:%M:%S:%p")
    label.config(text=string)
    label.after(1000,time)

label = Label(root,font=('sanserif'), background='black', foreground= 'cyan')
label.pack(anchor='center')

time()
mainloop()