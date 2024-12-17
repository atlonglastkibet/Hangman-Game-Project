import random
import turtle

# List of possible words for the game
words = [
    'kisumu', 'nairobi', 'eldoret', 'nakuru', 'kakamega',
    'mombasa', 'kitale', 'bomet', 'nyeri', 'muranga', 'turkana',
    'kwale', 'mtwapa', 'kilifi', 'kiserian', 'rongai', 'busia',
    'naivasha', 'machakos', 'kitui', 'garissa', 'moyale', 'thika',
    'meru', 'vihiga', 'bungoma', 'isiolo', 'marsabit', 'voi', 'embu',
    'kiambu', 'makueni', 'wajir', 'limuru'
]

# Turtle setup for drawing hangman
screen = turtle.Screen()
screen.title("Hangman Game: Kenyan Edition")
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)

# Draw the gallows for hanging the person
def draw_gallows():
    drawer.penup()
    drawer.goto(-100, -150)
    drawer.pendown()
    drawer.forward(200)  # Base
    drawer.backward(100)
    drawer.left(90)
    drawer.forward(300)  # Pole
    drawer.right(90)
    drawer.forward(100)  # Beam
    drawer.right(90)
    drawer.forward(30)   # Rope

# Draw parts of the hangman person
def draw_hangman(attempts_left):
    parts = {
        5: lambda: drawer.penup() or drawer.goto(80, 100) or drawer.pendown() or drawer.circle(20),  # Head (move the head to align with the body)
        4: lambda: drawer.penup() or drawer.goto(100, 80) or drawer.pendown() or drawer.goto(100, 0),  # Body
        3: lambda: drawer.penup() or drawer.goto(100, 80) or drawer.pendown() or drawer.goto(120, 50),  # Left Arm
        2: lambda: drawer.penup() or drawer.goto(100, 80) or drawer.pendown() or drawer.goto(80, 50),   # Right Arm
        1: lambda: drawer.penup() or drawer.goto(100, 0) or drawer.pendown() or drawer.goto(120, -50),  # Left Leg
        0: lambda: drawer.penup() or drawer.goto(100, 0) or drawer.pendown() or drawer.goto(80, -50)    # Right Leg
    }
    if attempts_left in parts:
        parts[attempts_left]()  # Draw the appropriate part

# Function to choose a random word
def choose_word():
    return random.choice(words)

# Initialize the game variables
def initialise_game(word):
    guessed_letters = set()  # Store the guessed letters
    attempts = 6  # Maximum number of attempts
    return guessed_letters, attempts

# Display the word progress
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Get user input
def get_guess():
    return input("Guess a letter: ").lower()

# Update game state
def update_game_state(guess, word, guessed_letters, attempts):
    if guess in guessed_letters:
        print("You already guessed that letter!")
    elif guess in word:
        guessed_letters.add(guess)
        print("Good guess!")
    else:
        guessed_letters.add(guess)
        attempts -= 1
        print("Wrong guess!")
        draw_hangman(attempts)  # Draw a part of the hangman
    return guessed_letters, attempts

# Check if the player has won or lost
def check_game_status(word, guessed_letters, attempts):
    if all(letter in guessed_letters for letter in word):
        print(f"Congratulations! You guessed the word: {word}")
        return True
    elif attempts == 0:
        print(f"Game over! The word was: {word}")
        return True
    return False

# Main game loop
def play_hangman():
    word = choose_word()
    guessed_letters, attempts = initialise_game(word)

    print("Welcome to Hangman! \nKenyan Towns & Cities Edition")
    print(display_word(word, guessed_letters))
    draw_gallows()  # Draw the gallows
    
    while True:
        print(f"Attempts remaining: {attempts}")
        guess = get_guess()

        guessed_letters, attempts = update_game_state(guess, word, guessed_letters, attempts)
        print(display_word(word, guessed_letters))
        
        if check_game_status(word, guessed_letters, attempts):
            break

    # Keep the turtle screen open until clicked
    screen.exitonclick()

# Main function
if __name__ == "__main__":
    play_hangman()
