__author__ = 'amendrashrestha'

import random
import time

import utilities as util

"""This is the main class of hang-me-not project"""

class HangMeNot(object):

    def __init__(self):
        self.print_game_name()
        self.play_again = True

        self.player_name = UserProfile()
        print("Welcome " + self.player_name.username + ". All the best!!! \n ** Press 1 for hint ** \n" )

        while self.play_again:
            self.start_game()

# Printig the name of the project
    def print_game_name(self):
        print("**************************************************************************************************")
        time.sleep(0.4)
        print("*  ____  ____                               ____    ____               ____  _____          _    *")
        time.sleep(0.4)
        print("* |_   ||   _|                             |_   \  /   _|             |_   \|_   _|        / |_  *")
        time.sleep(0.4)
        print("*   | |__| |   ,--.   _ .--.   .--./) ______ |   \/   |  .---.   ______ |   \ | |   .--.  `| |-' *")
        time.sleep(0.4)
        print("*   |  __  |  `'_\ : [ `.-. | / /'`\;|______|| |\  /| | / /__\\\ |______|| |\ \| |  / .'`\ \| |   *")
        time.sleep(0.4)
        print("*  _| |  | |_ // | |, | | | | \ \._//       _| |_\/_| |_| \__.,        _| |_\   |_ | \__. || |,  *")
        time.sleep(0.4)
        print("* |____||____|\'-;__/[___||__].',__`        |_____||_____|'.__.'       |_____|\____| '.__.' \__/  *")
        time.sleep(0.4)
        print("*                             ( ( __))                                                           *")
        time.sleep(0.4)
        print("**************************************************************************************************")

# Starting the game
    def start_game(self):
        self.word_to_guess = self.return_word_to_guess()
        # print("Actual word: " + self.word_to_guess)
        self.hangman_word = " ".join(self.randomize_word_letter(self.word_to_guess))
        self.play_game(self.hangman_word, self.word_to_guess)

# Drawing hangman graphics
    @property
    def draw_hangman(self):
        hangman = [
            '  |---||   \n  |   ||   \n      ||   \n      ||   \n      ||   \n      ||   \n========= \n',
           '  |---||   \n  |   ||   \n  0   ||   \n      ||   \n      ||   \n      ||   \n========= \n',
            '  |---||   \n  |   ||   \n  0   ||   \n  |   ||   \n      ||   \n      ||   \n========= \n',
            '  |---||   \n  |   ||   \n  0   ||   \n /|   ||   \n      ||  \n      ||   \n========= \n',
            '  |---||   \n  |   ||   \n  0   ||   \n /|\\  ||   \n      ||   \n      ||   \n========= \n',
            '  |---||   \n  |   ||   \n  0   ||   \n /|\\  ||   \n /    ||   \n      ||   \n========= \n',
           '  |---||   \n  |   ||   \n  0   ||   \n /|\\  ||   \n / \\  ||   \n      ||   \n========= \n'
        ]
        return hangman

# This method choses the random word to guess from the list of words
    def return_word_to_guess(self):
        handle = open("word_list.csv", "rb")
        self.word_dict = {}

        for row in handle:
            word_row = row.split(";")
            self.word_dict[word_row[0]] = word_row[1].replace("\r","").replace("\n","")

        return random.choice(self.word_dict.keys())

# This method is responsible for playing hang-me-not game.
# This method takes word to guess and the actual word.
# Here

    def play_game(self, word_to_guess, actual_word):
        self.hangman_graphic = self.draw_hangman
        guessed_letters = ""
        wrong_guesses = 0
        hangman_size = len(self.hangman_graphic)
        word_list = list(word_to_guess.replace(" ",""))

        while wrong_guesses < hangman_size:
            print("Word to guess: " + " ".join(word_to_guess))
            print("Letters guessed: " + guessed_letters)

            if "_" not in word_to_guess:
                print("Congratulations!!! You won!")
                self.return_play_again_choice()

            guess = self.return_guess(actual_word, guessed_letters)

            if guess in actual_word:
                print("Correct guess!!!")
                word_to_guess = self.renew_word_to_guess_list(guess, word_list, actual_word)
                guessed_letters += guess + " "
            else:
                guessed_letters += guess + " "
                print(self.hangman_graphic[wrong_guesses])
                wrong_guesses += 1

                guess_remaining = hangman_size - wrong_guesses
                print("Wrong Guess. You have %i guesses remaining !!!" % guess_remaining)

                if wrong_guesses == hangman_size:
                    print("Sorry, you lost the game!")
                    print("The word to guess was: " + actual_word)
                    self.return_play_again_choice()

# This method checks if the guess made by player exists in the acutal word or not.
# If it exists it replaces the "_" character in actual word with the guess letter.
    def renew_word_to_guess_list(self, guess, word, actual_word):
        for letter in range(len(actual_word)):
            if actual_word[letter] == guess:
                word[letter] = guess
                letter += 1
            else:
                letter += 1
        return word

# This method checks user input.
# Inform users to write valid inputs only.
    def return_guess(self, actual_word, guessed_letters):
        while True:
            user_input = raw_input().lower()
            if len(user_input) != 1:
                print("Please enter only one character!")
            elif user_input == "1":
                self.get_hint(actual_word)
            elif user_input in guessed_letters:
                print("The letter is already used!")
            elif user_input not in "abcdefghijklmnopqrstuvwxyz1":
                print("Please enter either character or 1!")
            else:
                return user_input

# This method takes acutal word and replace some of the letter with "_".
# These "_" are the places where user should guess the letter to complete
# the actual word. 90% of acutal word is replaced with "_"
    def randomize_word_letter(self, word_to_random):
        list_word = list(word_to_random)
        aux = range(len(word_to_random))

        number_to_replace = int(0.9 * len(list_word))

        while number_to_replace >= 0:
            posit = random.randrange(len(aux))
            list_word[posit] = "_"
            number_to_replace -= 1
        return list_word

# This method returns the hint of the actual word.
# If user wishes to get hint by press 1.
    def get_hint(self, word):
        word_hint = self.word_dict.get(word)
        print("Hint: " + word_hint)

# Once the game is completed. This method takes the user's choice if
# he/she wants to play the game again. If yes it will restart the game
# with welcome message. If the user doesn't want to replay the game
# the game exists with Have a nice day message.
    def return_play_again_choice(self):
        choice = raw_input("\nWould you like to play again? [Y/N]\n>")

        if choice.lower() not in 'y':
            print("Have a nice day %s !!!" %self.player_name.username)
            self.play_again = False
            quit()
        else:
            print("Welcome back %s" %self.player_name.username)
            self.start_game()

"""This is the player class of hang-me-not project.
A user can create his profile and continue to play the game.
If the username already exists in the system, the player is made
aware of it and suggested to choose another unique username."""

class UserProfile(object):
    def __init__(self):
        self.username = self.get_username

#Getting username of the player and storing in the file
    @property
    def get_username(self):
        player_file_path = "player_names.txt"
        self.player_name = raw_input("\n Enter player name: ")

        temp_player_name = self.check_player_name(self.player_name, player_file_path)

        if temp_player_name:
            util.write_into_file(player_file_path, self.player_name)
        else:
            print("** Player name " + self.player_name + " already exists. Please choose another username!! **")
            self.get_username

        return self.player_name

#Checks if username already exists.
    def check_player_name(self, name, file_path):
        self.player_name = name.lower()

        handle = open(file_path, 'rb')
        players = [line.strip().lower() for line in handle]

        if self.player_name in players:
            return False
        return True

#############################
HangMeNot()





