secret_word = "green";
guess = None;
no_of_guesses = 3;

while(secret_word != guess and no_of_guesses != 0): # loop will continue to run while the guess is wrond and no of guesses is not 0
    guess = input("Enter a guess word: ");

    if(secret_word == guess):
        print("You win!");
    else:
        no_of_guesses -= 1;
        print(f"Oops! Incorrect. You have {no_of_guesses} tries left");

if(no_of_guesses == 0): # boolean statement printing a statement if user loses the game (out of guesses)
    print("You lose! Git gud")
