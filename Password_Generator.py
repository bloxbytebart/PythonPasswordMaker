import tkinter as q
import random
import string

def generate_password():
    length = int(l_entry.get())
    charecters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(charecters)

    resultlbl.config(text=password)


window = q.Tk()
window.title("Password Generator")
window.geometry("300x200")

title = q.Label(window, text="Password Generator")
title.pack()

greytext = q.Label(window, fg ="grey",text="Please enter the number of digits", width=50, height = 1)
greytext.pack()
l_entry = q.Entry(window)
l_entry.pack()

generateBTN = q.Button(window, fg="blue", bg="white", text="generate", command=generate_password)
generateBTN.pack()

resultlbl = q.Label(window, text="")
resultlbl.pack()

window.mainloop()