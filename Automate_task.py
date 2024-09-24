import tkinter as tk
from tkinter import Entry, Label , Button
import webbrowser

#define the function to automate google search
root = tk.Tk()
root.title("YOUR AI ASSISTANT")

#adding background color

root.configure(bg="red")

#define the function to automate youtube search

def search_youtube():
  query = entry.get()
  url = "https://www.youtube.com/results?search_query={query}"
  webbrowser.open(url)

#define the function to automate goole search

def search_goole():
  query = entry.get()
  url = "https://www.goole.com/search?={query}"
  webbrowser.open(url)

  

#define the function to automate instagram search

def search_instagram():
  Username = entry.get().replace('@'," ") #Ensure username is clean of @
  url ="www.instagram.com/{username}/"
  webbrowser.open(url)


#create input field lables and buttons
Label(root , text="Enter your command").pack(pady=10)

#here root means only show the window

entry =Entry(root , width=50)
entry.pack(pady=10)
Button(root, text="Search on youtube" , command=search_youtube).pack(pady=10)
Button(root, text="Search on google" , command=search_goole).pack(pady=10)
Button(root, text="Search on instagram" , command=search_instagram).pack(pady=10)

#Run th GUI event loop
root.mainloop()

