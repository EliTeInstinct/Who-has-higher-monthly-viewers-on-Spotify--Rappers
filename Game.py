import tkinter as tk
import random
window = tk.Tk()
window.title("Higher or Lower")
window.geometry("1200x1200")

def show_screen(frame):
    for f in frames:
        f.pack_forget()  # Hide all screens/frames
    menu_screen.pack_forget()
    frame.pack(fill="both", expand=True)  # Shows the selected screen/frame
    window.update_idletasks()

def show_random_frame():
    #Pick a random screen/frame and displays it without repeating the last one. Work in Progress
    global last_shown_frame
    # This is an attempt to not display previous screens that have already been displayed
    available_frames = [frame for frame in frames if frame != last_shown_frame]

    # Pick a random frame from the available ones
    random_frame = random.choice(available_frames)

    show_screen(random_frame) 
    last_shown_frame = random_frame 
last_shown_frame = None

def back_to_menu():
    show_screen(menu_screen)

def random_screen():
    # Picks a random screen/frame then displays it
    random_frame = random.choice([game_screen, screen, screen2,screen3, screen4])
    show_screen(random_frame)
    random_frame.update_idletasks()

# This is a temporary logo
logo = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/logo.png")
# Rapper images 
kanye = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/ye.png")
kendrick= tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/lamar.png")  
uzi = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/liluzi.png")  
jack = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/jack.png")
travis = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/travis.png")
eminem = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/eminem.png")
ice_cube = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/cube.png")
juice_wrld = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/juice.png")
lilwayne = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/lilwayne.png")
nicki  = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/nicki.png")
postmalone = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/postmalone.png")
snoop  = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/snoopdogg.png")
tripie_redd= tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/tripie.png")
jayz = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/JayZ.png")
savage21 = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/21Savage.png")
bad_bunny = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/BadBunny.png")
drake = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/Drake.png")
xxxtentacion  = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/x.png")
tyler = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/tyler.png")
playboicarti = tk.PhotoImage(file="/Users/christian/Desktop/UpdatedPhotos/carti.png")

last_shown_frame = None
# Menu screen
menu_screen = tk.Frame(window)
menu_label = tk.Label(menu_screen, text="Menu Screen", font=("Arial", 18))
menu_label.pack(pady=10)
menu_image_label = tk.Label(menu_screen, image=logo)  # Display the menu image
menu_image_label.pack(pady=10)
start = tk.Button(menu_screen, text="Start Game", command=show_random_frame)
start.pack()

#start_button = tk.Button(menu_screen, text="Start Game", command=show_game)
#start_button.pack()

# Game screen
game_screen = tk.Frame(window)
game_image_label = tk.Label(game_screen, image=kanye) #enter rapper image to the left
game_image_label.place(x=0,y=0)
game_image_label2 = tk.Label(game_screen, image=kendrick) #enter rapper image to the left
game_image_label2.place(x=800,y=0)
game_label = tk.Label(game_screen, text="Score", font=("Arial", 18))
game_label.place(x=0,y=0)

button_next0 = tk.Button(game_screen, text="Higher", command=show_random_frame)
button_next0.place(x=750,y=500)
incorrect_answer0 = tk.Button(game_screen, text="Lower", command=back_to_menu).place(x=750,y=400)
return_back = tk.Button(game_screen, text="Back to Main Menu", command=back_to_menu).place(x=250,y=350)

label_question = tk.Label(game_screen, text="Does Kendrick have higher monthly Spotify listners than Kanye?",font=('Arial',18))
label_question.place(x=200,y=50)

# Next screen 
screen = tk.Frame(window)
image_label = tk.Label(screen, image=uzi) #enter rapper image to the left
image_label.place(x=800,y=0)
image_labela = tk.Label(screen, image=jack) #enter rapper image to the left
image_labela.place(x=0,y=0)
button_next1 = tk.Button(screen, text="Higher", command=show_random_frame).place(x=750,y=500)
incorrect_answer = tk.Button(screen, text="Lower", command=back_to_menu).place(x=750,y=400)

label_question = tk.Label(screen, text="Does Lil uzi Vert have higher monthly Spotify listners than Jack Harlow?",font=('Arial',18))
label_question.place(x=200,y=50)

# This brings you back to the maain menu if you selected a wrong answer

# Screen 2
screen2 = tk.Frame(window)
image_label2 = tk.Label(screen2, image=eminem).place(x=0,y=0)
image_labelb = tk.Label(screen2, image=travis).place(x=800,y=0)
button_next2 = tk.Button(screen2, text="Higher", command=show_random_frame)
button_next2.place(x=750,y=400)
incorrect_answer2 = tk.Button(screen2, text="Lower", command=back_to_menu).place(x=750,y=500)

label_question = tk.Label(screen2, text="Does Eminem have higher monthly Spotify listners than Travis Scott?",font=('Arial',18))
label_question.place(x=200,y=50)
# Screen 3
screen3 = tk.Frame(window)
image_label3 = tk.Label(screen3, image=nicki).place(x=0,y=0)
image_labelc = tk.Label(screen3, image=bad_bunny).place(x=800,y=0)

incorrect_answer3 = tk.Button(screen3, text="Higher", command=back_to_menu).place(x=750,y=500)
button_next3 = tk.Button(screen3, text="Lower", command=show_random_frame)
button_next3.place(x=750,y=400)

label_question = tk.Label(screen3, text="Does Nicki Minaj have higher monthly Spotify listners than Bad Bunny?",font=('Arial',18))
label_question.place(x=200,y=50)
# Screen 4
screen4 = tk.Frame(window)
image_label4 = tk.Label(screen4, image=juice_wrld).place(x=0,y=0)
image_labeld = tk.Label(screen4, image=postmalone).place(x=800,y=0)

incorrect_answer4 = tk.Button(screen4, text="Higher",command=back_to_menu).place(x=750,y=500)

button_next4 = tk.Button(screen4, text="lower", command=show_random_frame)
button_next4.place(x=750,y=400)

label_question = tk.Label(screen4, text="Does Juice Wrldd have higher monthly Spotify listners than Post Malone?",font=('Arial',18))
label_question.place(x=200,y=50)
# Screen 5
screen5 = tk.Frame(window)
image_label5 = tk.Label(screen5, image=tripie_redd).place(x=0,y=0)
image_labele = tk.Label(screen5, image=ice_cube).place(x=800,y=0)

incorrect_answer5 = tk.Button(screen5, text="Higher",command=back_to_menu).place(x=750,y=500)
button_next5 = tk.Button(screen5, text="Lower", command=show_random_frame).place(x=750,y=400)

label_question = tk.Label(screen5, text="Does Triple Redd have higher monthly Spotify listners than Ice Cube?",font=('Arial',18))
label_question.place(x=200,y=50)


# Screen 7
screen7 = tk.Frame(window)
image_label7 = tk.Label(screen7, image=savage21).place(x=0,y=0)
image_labelg = tk.Label(screen7, image=snoop).place(x=800,y=0)

incorrect_answer7 = tk.Button(screen7, text="Lower",command=back_to_menu).place(x=750,y=400)
button_next7 = tk.Button(screen7, text="Higher", command=show_random_frame).place(x=750,y=500)

label_question = tk.Label(screen7, text="Does 21 Savage have higher monthly Spotify listners than Snoop Dogg?",font=('Arial',18))
label_question.place(x=200,y=50)

#Screen8
screen8 = tk.Frame(window)
image_label8 = tk.Label(screen8, image=jayz).place(x=0,y=0)
image_labelh = tk.Label(screen8, image=lilwayne).place(x=800,y=0)

incorrect_answer8 = tk.Button(screen8, text="Higher",command=back_to_menu).place(x=750,y=500)
button_next8 = tk.Button(screen8, text="Lower", command=show_random_frame).place(x=750,y=400)

label_question = tk.Label(screen8, text="Does Jayz have higher monthly Spotify listners than Lil Wayne?",font=('Arial',18))
label_question.place(x=200,y=50)

# Screen 9
screen9 = tk.Frame(window)
image_label9 = tk.Label(screen9, image=xxxtentacion).place(x=0,y=0)
image_labeli = tk.Label(screen9, image=drake).place(x=800,y=0)

incorrect_answer9 = tk.Button(screen9, text="Higher",command=back_to_menu).place(x=750,y=500)
button_next9 = tk.Button(screen9, text="Lower", command=show_random_frame).place(x=750,y=400)

label_question = tk.Label(screen9, text="Does xxxtentaction have higher monthly Spotify listners than drake?",font=('Arial',18))
label_question.place(x=200,y=50)
# Screen 10
screen10 = tk.Frame(window)
image_label10 = tk.Label(screen10, image=playboicarti).place(x=0,y=0)
image_labelj = tk.Label(screen10, image=tyler).place(x=800,y=0)

incorrect_answer10 = tk.Button(screen10, text="Lowerr",command=back_to_menu).place(x=750,y=400)
button_next10 = tk.Button(screen10, text="Higher", command=show_random_frame).place(x=750,y=500)

label_question = tk.Label(screen10, text="Does PlayBoi Carti have higher monthly Spotify listners than tyler?",font=('Arial',18))
label_question.place(x=200,y=50)

frames = [game_screen, screen, screen2, screen3, screen4, screen5, screen7, screen8, screen9,screen10]
# Show the initial screen
menu_screen.pack(fill="both", expand=True)
# Run the main loop
