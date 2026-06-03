
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game using Python to practice string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️ Build the Game Loop

#### Description
Create the core Hangman game loop that selects a hidden word and allows the player to guess letters until the game ends.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Display the hidden word progress using `_` for unguessed letters
- Prompt the player to guess a single letter each turn
- Update the displayed word progress when the guess is correct
- Track and display incorrect guesses remaining

### 🛠️ Handle Game End Conditions

#### Description
Add win and loss logic so the game ends with the correct message when the player wins or runs out of attempts.

#### Requirements
Completed program should:

- End the game when the player guesses all letters correctly
- End the game when the player uses all allowed incorrect guesses
- Display a win message when the word is fully guessed
- Display a loss message when the player fails to guess the word in time

### 🛠️ Add User Feedback

#### Description
Improve the player experience by showing guess results and the current game state clearly.

#### Requirements
Completed program should:

- Show the current progress after each guess
- Display the list of letters already guessed
- Inform the player when a guess is correct or incorrect
- Avoid counting repeated guesses as new incorrect attempts
