import tkinter as tk

window = tk.Tk()
window.geometry("300x300")

label_1 = tk.Label(window, text="Enter a sentence with at least 10 letters")
label_1.pack()

entry_1 = tk.Entry(window)
entry_1.pack()

label_2 = tk.Label(window)  # This will be used to show the sentence length

def func_1():
    var = entry_1.get()
    if len(var) >= 10:
        label_2.config(text="The length of your sentence is " + str(len(var)))
    else:
        label_2.config(text="Please enter at least 10 characters.")

    label_2.pack()

j_button = tk.Button(window, text="Button", command=func_1)
j_button.pack()

window.mainloop()
