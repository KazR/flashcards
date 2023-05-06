import pandas as pd
import random
import tkinter as tk

# File path of the flashcards Excel file
file_path = "data/TestCards.xlsx"

# Load the flashcards from the Excel file
flashcards = pd.read_excel(file_path)

# Create a Tkinter window
window = tk.Tk()
window.geometry("325x325")  # Set the window size to 400x400
window.config(bg="#A2D2FF")

# Declare the back variable as global
back = ""
previous_card = None
is_swapped = False
correct_answers = 0
attempted_answers = 0


def display_flashcard():
    global front, back, previous_card, correct_answers, attempted_answers
    result_label.config(bg="#A2D2FF")
    # Randomly select a row
    rows = flashcards.index.tolist()
    if previous_card is not None:
        rows.remove(previous_card)
    row = random.choice(rows)
    previous_card = row

    # Get the front and back values from the selected row
    front = flashcards.loc[row, "front"]
    back = flashcards.loc[row, "back"]

    # Update the flashcard window
    window.title("Flashcard Application")
    if is_swapped:
        front_label.config(text=back, bg="#A2D2FF", fg="#FFFFFF", font=("Helvetica, 32"))
    else:
        front_label.config(text=front, bg="#A2D2FF",fg="#FFFFFF", font=("Helvetica, 32"))
    entry.delete(0, tk.END)
    result_label.config(text="")
    check_button.config(text="Check Answer", bg="#BDE0FE", fg="#123123", font=("Helvetica, 12"), activebackground="#A2D2FF")
    check_button.unbind('<Return>')
    check_button.bind('<Return>', handle_check)
    check_button.config(command=check_answer)
    check_button.focus_set()
    # Update the attempted answers counter
    attempted_answers += 1


def check_answer():
    global back, is_swapped, correct_answers
    user_answer = entry.get().lower()
    result_label.config(font=("Helvetica", 12), bg="#A2D2FF")
    if is_swapped:
        correct_side = front
    else:
        correct_side = back
    if user_answer == correct_side.lower():
        correct_answers += 1
        result_label.config(text="Correct!", bg="#bde0fe",fg="#3D9970")
    else:
        result_label.config(text="Wrong! The correct answer is: " + correct_side, bg="#bde0fe", fg="#FF5733")
    score_label.config(text=f"{correct_answers} / {attempted_answers}")
    check_button.config(text="Next")
    check_button.focus_set()
    check_button.unbind('<Return>')
    check_button.bind('<Return>', handle_next)
    check_button.config(command=display_flashcard)
    


def swap_flashcard():
    global front, back, is_swapped
    is_swapped = not is_swapped
    if is_swapped:
        front_label.config(text=back)
    else:
        front_label.config(text=front)


def handle_check(event):
    check_answer()


def handle_next(event):
    display_flashcard()
    entry.focus_set()


# Display the front label
front_label = tk.Label(window)
front_label.pack(pady=10)

# User input for the answer
entry = tk.Entry(window, font=("Helvetica", 16))
entry.pack(pady=10)

# Bind the Enter key to the entry widget for both check and next actions
entry.bind('<Return>', handle_check)

# Button to check the answer or display the next flashcard
check_button = tk.Button(window, text="Check Answer", command=check_answer)
check_button.pack(pady=10)
check_button.bind('<Return>', handle_check)

# Label to display the result
result_label = tk.Label(window, text="", bg="#A2D2FF")
result_label.pack(pady=10)

# Label to display the score
score_label = tk.Label(window, text="0 / 0", bg="#A2D2FF", font=("Helvetica", 10))
score_label.pack(pady=10)


# Button to swap the front and back of the flashcard
swap_button = tk.Button(window, text="Swap", command=swap_flashcard, bg="#FFC8DD", font=("Helvetica, 12"), activebackground="#FFAFCC")
swap_button.pack(pady=10)

# Start the flashcard application
display_flashcard()

# Run the Tkinter event loop
window.mainloop()