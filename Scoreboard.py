# Initialize score
score = 0

def update_score(points):
    """Update the score by adding points."""
    global score
    score += points
    display_score()  # Update the score label dynamically

def display_score():
    """Display the current score"""
    score_label.config(text=f"Score: {score}")


    #score top left 

score_label = tk.label(game_screen, text=f"score: {score}", font=("Arial", 16), bg="lightgray")
score_label.place(x=250, y=250) #Scoreboard gonna shown top left 

button_next0 = tk.Button(game_screen, text="Higher", command=lambda: [update_score(10), show_random_frame()])
button_next0.place(x=250, y=250)
incorrect_answer0 = tk.Button(game_screen, text="Lower", command=back_to_menu).place(x=400, y=400)
return_back = tk.Button(game_screen, text="Back to Main Menu", command=back_to_menu).place(x=250, y=350)
