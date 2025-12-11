# Hangman
A classic word-guessing game built in Python. The player attempts to guess a hidden word one letter at a time while avoiding too many wrong guesses. Includes error handling, win/loss detection, and a visual representation of progress.

## Features

  Random word selection from a word list
  
  Tracks guessed letters and remaining attempts
  
  Input validation (single letters only)
  
  Displays current progress (e.g., _ a _ _ m a n)
  
  Clean game loop for replaying

## What I Learned

  File handling for loading word lists
  
  Loop control for game state
  
  String manipulation and formatted output
  
  Designing a multi-step game flow

  ## How to Run
  Have file "hangman_words.txt" in repository as file input
  Python main.py

  ## Example Output:

  
-----------------------
----- Turn Status -----
Word: _ _ _ _ _ _ _
Guesses remaining: 7
Incorrect guesses:

Guess a single letter: a
a is correct!

----- Turn Status -----
Word: _ _ _ _ a _ _
Guesses remaining: 7
Incorrect guesses:

Guess a single letter:

## Future Improvements
Add graphical code for game

Add difficulty levels

Add hint feature
