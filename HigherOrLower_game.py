import tkinter as tk
import random


window = tk.Tk()
window.title("Screen Switch with Images")
window.geometry("800x800")


last_shown_frame = None
frames = []

def show_screen(frame):
    for f in frames:
        f.pack_forget()  
    frame.pack(fill="both", expand=True) 

def show_random_frame():
    global last_shown_frame
    available_frames = [frame for frame in frames if frame != last_shown_frame]
    if available_frames:
        random_frame = random.choice(available_frames)
        show_screen(random_frame)
        last_shown_frame = random_frame

def back_to_menu():
    show_screen(menu_screen)

try:
    logo = tk.PhotoImage(file="/Users/christian/Desktop/HigherOrLower/HigherOrLowerLogo.png")
    Drake = tk.PhotoImage(file="/Users/christian/Desktop/HigherOrLower/Drake.png")
    KayneWest = tk.PhotoImage(file="/Users/christian/Desktop/HigherOrLower/KayneWest.png")
    Kendrick = tk.PhotoImage(file="/Users/christian/Desktop/HigherOrLower/Kendrick.png")
    LilUziVert = tk.PhotoImage(file="/Users/christian/Desktop/HigherOrLower/LilUziVert.png")
except tk.TclError as e:
    print("Error loading images:", e)
    logo = Drake = KayneWest = Kendrick = LilUziVert = None

if not logo:
    print("Failed to load the logo image. Check the file path or format.")


menu_screen = tk.Frame(window)
menu_label = tk.Label(menu_screen, text="Menu Screen", font=("Arial", 18))
menu_label.pack(pady=10)
if logo:
    menu_image_label = tk.Label(menu_screen, image=logo)
    menu_image_label.pack(pady=10)
else:
    menu_label.config(text="Menu Screen (Logo not loaded)")
start_button = tk.Button(menu_screen, text="Start Game", command=show_random_frame)
start_button.pack(pady=20)


game_screen = tk.Frame(window)
if Drake and KayneWest:
    game_image_label = tk.Label(game_screen, image=Drake)
    game_image_label.place(x=350, y=0)
    game_image_label2 = tk.Label(game_screen, image=KayneWest)
    game_image_label2.place(x=0, y=0)
game_label = tk.Label(game_screen, text="Score", font=("Arial", 18))
game_label.place(x=300, y=0)
back_button = tk.Button(game_screen, text="Back to Main Menu", command=back_to_menu)
back_button.place(x=250, y=350)


screen = tk.Frame(window)
screen2 = tk.Frame(window)
screen3 = tk.Frame(window)
screen4 = tk.Frame(window)
if logo:
    screen4_label = tk.Label(screen4, image=logo)
    screen4_label.pack()

frames = [game_screen, screen, screen2, screen3, screen4]


menu_screen.pack(fill="both", expand=True)


window.mainloop()
