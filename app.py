import pandas as pd
import random

# File path of the flashcards Excel file
file_path = "TestCards.xlsx"

# Load the flashcards from the Excel file
flashcards = pd.read_excel("data/TestCards.xlsx")

def display_flashcard(previous_card=None):
    # Randomly select a row excluding the previous card
    if previous_card is not None:
        rows = flashcards.index[flashcards.index != previous_card]
        row = random.choice(rows)
    else:
        row = random.choice(flashcards.index)

    # Get the front and back values from the selected row
    front = flashcards.loc[row, "front"]
    back = flashcards.loc[row, "back"]

    # Display the front of the flashcard
    print("Front of the card:", front)

    # Prompt the user for their answer
    answer = input("What is on the back of the card? ")

    # Check if the answer is correct (case-insensitive comparison)
    if answer.lower() == back.lower():
        print("Correct!")
    else:
        print("Wrong! The correct answer is:", back)

    # Display a new flashcard (passing the current card as the previous card)
    print("-------------------")
    display_flashcard(row)

# Start the flashcard application
display_flashcard()
