from random_word import RandomWords
import string
from tools import hangman_graphic


def game():

    word = random_hangman_word(game_difficulty())
    list_of_guesses = list()
    print(list_of_guesses)
    blank_letters_init(word)
    guess_letter(list_of_guesses, word)


def game_difficulty():

    difficulty_list = ['easy', 'meadium', 'hard']
    difficulty = None

    while difficulty not in difficulty_list:

        difficulty = input("Choose one of the following difficulties: easy (4-6 letter's), "
                           "medium (7-10 letters), hard (11-14 letters) by typing in the name of the difficulty.")

    print('Selected difficulty: ' + difficulty)

    return difficulty


def random_hangman_word(difficulty):

    r = RandomWords()

    if difficulty == 'easy':
        hangman_word = r.get_random_word(minLength=4, maxLength=6)
    elif difficulty == 'medium':
        hangman_word = r.get_random_word(minLength=7, maxLength=10)
    else:
        hangman_word = r.get_random_word(minLength=11, maxLength=14)

    return hangman_word


def blank_letters_init(word_for_hangman):

    letter_list = list(word_for_hangman)
    blank_letter_list = list()

    for i in letter_list:
        blank_letter_list.append('_ ')

    blank_letters = "".join(blank_letter_list)

    return blank_letters


def guess_letter(list_of_guesses, word):
    word_letters = list(word)
    guess = ""

    #while len(guess) != 1 and guess not in list_of_guesses and guess not in list(string.ascii_lowercase):
    while len(guess) != 1 and guess not in list_of_guesses:

        guess = input("Guess a letter!")

        if len(guess) == 1:
            print("yoho")
            #if guess in word_letters:



            #contains

            list_of_guesses.append(guess)

            print(list_of_guesses)

            return list_of_guesses

        print('Not good format. Give a letter')


game()

