from tkinter import Label, Tk


root = Tk()

label = Label(root, text= "Hello, world!")
label2 = Label(root, text= "Hello, world!")

label.grid(row=0, column=0)
label2.grid(row=1, column=1)

root.mainloop()
