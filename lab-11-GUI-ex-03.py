#Jeffrey Ramirez, Arturo Rivera, Christian Zarseno Hernandez, Yener Lopez 

import tkinter
window = tkinter.Tk()
window.geometry("300x100")
def color_swap():
    button_1.configure(bg="black")
button_1 = tkinter.Button(window, text="Push Button", command=color_swap)
button_1.pack()
window.mainloop()