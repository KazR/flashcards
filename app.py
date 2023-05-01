import pandas as pd
import random
import tkinter as tk

# File path of the flashcards Excel file
file_path = "data/TestCards.xlsx"

# Load the flashcards from the Excel file
flashcards = pd.read_excel(file_path)

# Create a Tkinter window
window = tk.Tk()
window.geometry("250x200")  # Set the window size to 400x400

# Declare the back variable as global
back = ""
previous_card = None

# Function to check the user's answer and proceed to the next flashcard
def check_answer():
    global back
    user_answer = entry.get().lower()
    if user_answer == back.lower():
        result_label.config(text="Correct!", fg="green")
        check_button.config(text="Next", command=display_flashcard)
    else:
        result_label.config(text="Wrong! The correct answer is: " + back, fg="red")
        check_button.config(text="Next", command=display_flashcard)

def display_flashcard():
    global back, previous_card
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
    front_label.config(text="Front of the card: " + front)
    entry.delete(0, tk.END)
    result_label.config(text="")
    check_button.config(text="Check Answer", command=check_answer)
    window.update()

    # Set focus to the entry widget
    entry.focus_set()

# Display the front label
front_label = tk.Label(window, text="Front of the card:")
front_label.pack(pady=10)

# User input for the answer
entry = tk.Entry(window)
entry.pack(pady=10)

# Button to check the answer
check_button = tk.Button(window, text="Check Answer", command=check_answer)
check_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the flashcard application
display_flashcard()

# Run the Tkinter event loop
window.mainloop()
