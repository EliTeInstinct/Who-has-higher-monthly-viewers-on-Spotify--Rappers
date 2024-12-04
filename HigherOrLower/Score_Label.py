score_label = tk.Label(window, text=f"Score: {score}/10", font=("Arial", 16), bg="white")
score_label.place(x=700, y=10)

def update_score_label():
    score_label.config(text=f"Score: {score}/10")

def check_answer(is_correct):
    global score
    if is_correct:
        score += 1
        tk.messagebox.showinfo("Result", "Correct!")
    else:
        tk.messagebox.showinfo("Result", "Wrong!")
  
    if score > 10:
        score = 10
