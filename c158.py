variable1 = 5
variable2 = 10

try: 
    print(variable1)
    print(variable2)
    print(variable3)
    
except NameError:
    
    print("Variable 3 is undefined")
    
print(variable1 + variable2)

from tkinter import *
root = Tk()
root.title("Bad Geometry Error/GUI Error")

try:
    root.geometry("800")
except:
    print("This is a bad geometry error. This is because there is one dimension instead of two. Another dimension must be needed.")
    
root.mainloop()

from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Addition")
root.geometry("500x500")

userinput = Entry(root)
userinput.place(relx = 0.5, rely = 0.3, anchor = CENTER)

def additionfunc():
    num = 50
    userinputvalue = userinput.get()
    
    try:
        print(num + userinputvalue)
    except(TypeError):
        messagebox.showinfo("This code does not work because you cannot concatenate two different data types, such as a string and an integer. Convert the number into a string to fix the code.")

additionbtn = Button(root, text = "Add 50", command = additionfunc)
additionbtn.place(relx = 0.5, rely = 0.4, anchor = CENTER)

root.mainloop()