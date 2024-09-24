from tkinter import *
import random

root = Tk()
root.geometry("700*450")
root.title("Rool Dice")

lable =Lable(root, text="" ,font=("times",260))

def roll():
  dice=['\u2680' , '\u2681' ,'\u2682', '\u2683' ,'\u2684' ,'\u2685']
  lable.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
  lable.pack()

button =Button(root,text="lets roll............",width=40,height=5,font=10,bg="white" ,bad=2,command=roll)

button.pack(padx=10 ,pady=10)

root.mainloop()