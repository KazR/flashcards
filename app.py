import pandas as pd
import random

# Load the flashcards from the Excel file
flashcards = pd.read_excel("data/TestCards.xlsx")

def display_flashcard():
    # Randomly select a row
    row = random.choice(flashcards.index)

    # Get the front and back values from the selected row
    front = flashcards.loc[row, "front"]
    back = flashcards.loc[row, "back"]

    # Display the front of the flashcard
    print("Front of the card: ", front)

    # Prompt the user for their answer
    answer = input("What is on the back of the card? ")

    # Check if the answer is correct
    if answer == back:
        print("Correct!")
    else:
        print("Wrong! The correct answer is:", back)

    # Display a new flashcard
    print("-------------------")
    display_flashcard()

# Start the flashcard application
display_flashcard()