__author__ = 'amendrashrestha'

import random
import time

import utilities as util

class HangMeNot(object):

    def __init__(self):
        self.print_game_name()
        self.play_again = True

        self.player_name = UserProfile()
        print("Welcome " + self.player_name.username + ". All the best!!! \n ** Press 1 for hint ** \n" )

        while self.play_again:
            self.start_game()

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

    def start_game(self):
        self.word_to_guess = self.return_word_to_guess()
        self.play_game(self.word_to_guess)

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

    def return_word_to_guess(self):
        handle = open("word_list.csv", "rb")
        self.word_dict = {}

        for row in handle:
            word_row = row.split(";")
            self.word_dict[word_row[0]] = word_row[1].replace("\r","").replace("\n","")

        return random.choice(self.word_dict.keys())

    def play_game(self, word_to_guess):
        user_input = raw_input()

        if user_input == "1":
            self.get_hint(word_to_guess)
        else:
            print("Playing game!!!")
            self.hangman_graphic = self.draw_hangman

            guessed_letters = []

            word = " ".join(self.randomize_word_letter(word_to_guess))
            print(word)

            if user_input in word:
                pass

            player_attempts = len(self.hangman_graphic) - 1

            print(self.hangman_graphic[6])

            self.return_play_again_choice()

    def randomize_word_letter(self, word_to_random):
        list_word = list(word_to_random)
        aux = range(len(word_to_random))

        number_to_replace = int(0.7 * len(list_word))

        while number_to_replace > 0:
            posit = random.randrange(len(aux))
            list_word[posit] = "_"
            number_to_replace -= 1
        return list_word

    def get_hint(self, word):
        word_hint = self.word_dict.get(word)
        print("Hint: " + word_hint)

    def return_play_again_choice(self):
        choice = raw_input("\nWould you like to play again? [Y/N]\n>")

        if choice.lower() not in 'y':
            print("Have a nice day " + self.player_name.username + "!!!")
            self.play_again = False
        else:
            print("Playing again!!")
            self.start_game()


class UserProfile(object):
    def __init__(self):
        self.username = self.get_username

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

    def check_player_name(self, name, file_path):
        self.player_name = name.lower()

        handle = open(file_path, 'rb')
        players = [line.strip().lower() for line in handle]

        if self.player_name in players:
            return False
        return True

#############################
HangMeNot()





