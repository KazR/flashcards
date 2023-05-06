import pandas as pd
import random
import tkinter as tk

# File path of the flashcards Excel file
file_path = "data/TestCards.xlsx"

# Load the flashcards from the Excel file
flashcards = pd.read_excel(file_path)

# Create a Tkinter window
window = tk.Tk()
window.geometry("250x250")  # Set the window size to 400x400

# Declare the back variable as global
back = ""
previous_card = None
is_swapped = False


# Function to check the user's answer and proceed to the next flashcard
def check_answer():
    global back, is_swapped
    user_answer = entry.get().lower()
    if is_swapped:
        correct_side = front
    else:
        correct_side = back
    if user_answer == correct_side.lower():
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Wrong! The correct answer is: " + correct_side, fg="red")
    check_button.config(text="Next")
    check_button.focus_set()
    check_button.unbind('<Return>')
    check_button.bind('<Return>', handle_next)
    check_button.config(command=display_flashcard)


def handle_next(event):
    display_flashcard()

def display_flashcard():
    global front, back, previous_card

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
        front_label.config(text="Front of the card: " + back)
    else:
        front_label.config(text="Front of the card: " + front)
    entry.delete(0, tk.END)
    result_label.config(text="")
    check_button.config(text="Check Answer")
    check_button.unbind('<Return>')
    check_button.bind('<Return>', handle_check)
    check_button.config(command=check_answer)
    check_button.focus_set()
    


def handle_check(event):
    check_answer()

# Display the front label
front_label = tk.Label(window, text="Front of the card:")
front_label.pack(pady=10)

# User input for the answer
entry = tk.Entry(window)
entry.pack(pady=10)

# Bind the Enter key to the entry widget for both check and next actions
entry.bind('<Return>', handle_check)

# Button to check the answer or display the next flashcard
check_button = tk.Button(window, text="Check Answer", command=check_answer)
check_button.pack(pady=10)
check_button.bind('<Return>', handle_check)

def swap_flashcard():
    global front, back, is_swapped
    is_swapped = not is_swapped
    if is_swapped:
        front_label.config(text="Front of the card: " + back)
    else:
        front_label.config(text="Front of the card: " + front)
    
def handle_next(event):
    display_flashcard()
    entry.focus_set()

# Label to display the result
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Button to swap the front and back of the flashcard
swap_button = tk.Button(window, text="Swap", command=swap_flashcard)
swap_button.pack(pady=10)

# Start the flashcard application
display_flashcard()

# Run the Tkinter event loop
window.mainloop()
