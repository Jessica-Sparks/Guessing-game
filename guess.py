#building a guessing game
#create a secret word
secret_word = "Python"

#create a guess variable using the input statement

guess = input('Guess what the Secret Word is: ')

while guess != secret_word:
    print('Oops! Guess again.')
    guess = input('Try a new Guess:')
print('Yay! You guessed right. Great job!')