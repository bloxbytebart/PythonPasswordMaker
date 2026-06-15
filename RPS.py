import tkinter as tk
from PIL import Image, ImageTk
import time
import random

window = tk.Tk()
window.geometry("400x400")
window.title("Rock, Paper, Scissor")

Rock = ImageTk.PhotoImage(Image.open("Rock.png").resize((150, 200)))
Paper = ImageTk.PhotoImage(Image.open("Paper.png").resize((150, 200)))
Scissor = ImageTk.PhotoImage(Image.open("Scissor.png").resize((150, 200)))

choices = {"Rock":Rock,
           "Paper":Paper,
           "Scissor":Scissor
           }


imagetxt = tk.Label(window)
imagetxt.pack()
label = tk.Label(window, text="")
label.pack()
lastchoice=""
def computer_play():
    computerchoice = random.choice(list(choices.keys()))
    global lastchoice
    while computerchoice == lastchoice:
        computerchoice = random.choice(list(choices.keys()))
        lastchoice=computerchoice

    imagetxt.config(image=choices[computerchoice])
    label.config(text=[computerchoice])


Button = tk.Button(window, fg="red", text="Press to start!", command=computer_play)
Button.pack()
    
window.mainloop()
    



