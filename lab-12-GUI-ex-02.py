#Jeffrey Ramirez, Arturo Rivera, Christian Zarseno Hernandez, Yener Lopez 

import tkinter as tk

box = tk.Tk(className='Color Changer')
box.minsize(600,600)

Number_1 = tk.Listbox(box, selectmode=tk.SINGLE, height="6")
Number_1.insert(tk.END, 'red')
Number_1.insert(tk.END, 'blue')
Number_1.insert(tk.END, 'green')
Number_1.insert(tk.END, 'orange')
Number_1.insert(tk.END, 'cyan')
Number_1.insert(tk.END, 'gray')
Number_1.pack()
Number_1.select_set(0)

def setColor():
    picked = Number_1.curselection()
    temp_text = Number_1.get(picked)
    if temp_text == 'custom':
        setCustomColor()
    else:
        power.configure(text=temp_text)
        box.config(bg=temp_text)


power = tk.Button(box, text='Set Color', command=setColor)
home = tk.Label(box, text='your selection')

power.pack()

home.pack()
box.mainloop()