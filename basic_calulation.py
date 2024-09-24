import tkinter as tk
from tkinter import Entry, Label , Button

root = tk.Tk()
root.title("HERE BASIC AIRTHMATIC CALCUALTION:")
root.configure(bg="red")
def caculate():
  first_number =float( first_number.entry.get())
  second_number =float(second_number.entry.get())
  operation = operator.get()
  if operator == "*":
   result=first_number+second_number

  elif operator == "/":
    result=first_number/second_number;
   
  elif operator == "-":
    result=first_number-second_number;
   
  elif operator == "+":
    result=first_number+second_number;
  else:
    result="Invalid operation"
    
  result_label.config(text="Result :"+ str(result))
 
  Button(root, text="+" , command="calculate").pack(pady=10)
  Button(root, text="-" , command="calculate").pack(pady=10)
  Button(root, text="*" , command="calculate").pack(pady=10)
  Button(root, text="/" , command="calculate").pack(pady=10)
  root.mainloop()




  
  

