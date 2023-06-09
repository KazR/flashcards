# Flashcard Application

This is a simple flashcard application written in Python. It allows you to test your knowledge by presenting flashcards and checking your answers.

## Features

- Loads flashcards from an Excel file
- Randomly selects a flashcard and displays the front
- Prompts the user to provide the answer for the back of the card
- Checks if the answer is correct (case-insensitive)
- Displays the correct answer if the user's answer is wrong
- Will not display the same card twice
- Continues presenting new flashcards until the program is terminated
- Keeps track of your attempts and how many were correct


## Usage

1. Ensure you have Python 3 installed on your system.
2. Install the required dependencies by running `pip install pandas`.
3. Clone this repository to your local machine.
4. Place your flashcards in an Excel file, with two columns named "front" and "back".
5. Update the `file_path` variable in the code to point to your Excel file.
6. Run the application by executing `python flashcard.py`.
7. The application will randomly present flashcards and prompt you to provide the answer for the back of the card.
8. Your answer will be checked, and the correct answer will be displayed if necessary.
9. The program will continue presenting new flashcards until you terminate it.

Feel free to customize the code and Excel file to suit your needs!

## Author

This flashcard application was created by Kaz.

