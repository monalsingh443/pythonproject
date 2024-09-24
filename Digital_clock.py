import tkinter as tk
from time import strftime  #strftime is a python module which contain the time and date 

root =tk.Tk()
root.title("Digital Clock")  #here title define window

def time():
  string =strftime("%H: %M : %S %p \n %D")
  lable.config(text=string)
  lable.after(1000,time)  #here every second update ur time 

lable =tk.Label(root , font=('calibri',60,'bold'),background='yellow',foreground='red')
lable.pack(anchor='center')

time()

root.mainloop()    #here currently window run