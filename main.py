import os
os.chdir(input("Enter the path to your desired directory: "))

with open("intro.txt", "w+") as file:
    file.write("My name is Avyukt. I am a student and I like technology and coding.")
    print(file.read())

with open("intro.txt", "r") as file:
    words = file.read().split()
    print(words, "\nNumber of words in this file is", len(words))

if os.path.exists("My_File"):
    print("My_File exists")
else:
    with open("My_File", "w+") as file:
        file.write("""  Coding is basically the computer language used to develop apps, websites, and software. 
                    Without it, we’d have none of the most popular technology we’ve come to rely on such as Facebook, our smartphones, the browser. 
                    It all runs on code.
                    To put it very simply, the code is what tells your computer what to do. 
                    To go a bit deeper, computers don’t understand words. 
                    They only understand the concepts of on and off.  
                    Binary code represents these on and off signals as the digits 1 and 0. 
                    In order to make binary code manageable, computer programming languages were formed. """)
        
    print("My_File created")
    print(file.read())

if os.path.exists("intro.txt"):
    os.remove("intro.txt")
    print("intro.txt deleted")
else:
    print("intro.txt does not exist")

file.close()