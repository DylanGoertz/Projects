import random
import os
import time

class HangmanGame:
    def __init__(self):
        self.words = [
            "python", "programming", "computer", "algorithm", "dictionary",
            "variable", "function", "hangman", "keyboard", "developer", 
            "software", "database", "network", "interface", "system"
        ]
        self.word = ""
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_attempts = 6

    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def select_word(self):
        """Randomly select a word from the word list."""
        self.word = random.choice(self.words)
        
    def display_word(self):
        """Display the word with unguessed letters replaced by underscores."""
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()

    def display_hangman(self):
        """Display the hangman figure based on incorrect guesses."""
        stages = [
            """
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |      |
               |      
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |     /|
               |      
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |      
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |     / 
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |     / \\
               |     
               -
            """
        ]
        return stages[self.incorrect_guesses]

    def play(self):
        """Main game loop."""
        self.select_word()
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        
        while True:
            self.clear_screen()
            print("\n=== HANGMAN GAME ===\n")
            print(self.display_hangman())
            print("\nWord:", self.display_word())
            print(f"Guessed letters: {', '.join(sorted(self.guessed_letters)) if self.guessed_letters else 'None'}")
            print(f"Incorrect guesses: {self.incorrect_guesses}/{self.max_attempts}")
            
            # Check if player has won
            if all(letter in self.guessed_letters for letter in self.word):
                print("\nCongratulations! You guessed the word:", self.word)
                break
                
            # Check if player has lost
            if self.incorrect_guesses >= self.max_attempts:
                print("\nGame Over! The word was:", self.word)
                break
                
            # Get player's guess
            guess = input("\nGuess a letter: ").lower()
            
            # Validate input
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                time.sleep(1)
                continue
                
            # Check if letter has already been guessed
            if guess in self.guessed_letters:
                print("You already guessed that letter.")
                time.sleep(1)
                continue
                
            # Add letter to guessed letters
            self.guessed_letters.add(guess)
            
            # Check if guess is correct
            if guess in self.word:
                print("Good guess!")
            else:
                print("Incorrect guess.")
                self.incorrect_guesses += 1
            
            time.sleep(1)
        
        # Ask if player wants to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again == 'y':
            self.play()
        else:
            print("Thanks for playing! Goodbye.")


if __name__ == "__main__":
    game = HangmanGame()
    game.play()