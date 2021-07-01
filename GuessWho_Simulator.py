'''
Author: Advait Rao
Date: 26-05-2021
GuessWhoSimulator.py: This program runs simulations of the board game Guess Who.
'''
########################################################
# THIS CLASS CREATES A character IN THE GAME OF GUESS WHO #
########################################################

# name (String)  : The first name of the character
# gender (String) : The character's gender
# facial_hair (String) : moustache, beard or None
# hair_colour (String) : Black, Blonde, Red, Brown or None
# hair_length (String) : Short, Long or Bald
# hair_style : Straight or Curly
# glasses (boolean) : Does the character wear glasses?
# earrings (boolean) Does the character wear earrings?
# nose_size (String) : Small, Medium, Large
# red_cheeks (boolean) : Does the character have red cheeks?
# blue_eyes (boolean) : Does the character have blue eyes?
# sad (boolean) : Does the character look sad?


class Character:
    def __init__(self, name, female, facial_hair, moustache, beard, black_hair,
                ginger_hair, blonde_hair, brown_hair, white_hair,
                hair_partition, curly_hair, hat, bald, long_hair, glasses,
                earrings, big_nose, big_mouth, red_cheeks, blue_eyes, sad):

        self.__name = name
        self.__traits_dict = {
            "female": female,
            "facial_hair": facial_hair,
            "moustache": moustache,
            "beard": beard,
            "black_hair": black_hair,
            "ginger_hair": ginger_hair,
            "blonde_hair": blonde_hair,
            "brown_hair": brown_hair,
            "white_hair": white_hair,
            "hair_partition": hair_partition,
            "curly_hair": curly_hair,
            "hat": hat,
            "bald": bald,
            "long_hair": long_hair,
            "glasses": glasses,
            "earrings": earrings,
            "big_nose": big_nose,
            "big_mouth": big_mouth,
            "red_cheeks": red_cheeks,
            "blue_eyes": blue_eyes,
            "sad": sad
        }

        for key in self.__traits_dict:
            if self.__traits_dict[key] == "F":
                self.__traits_dict[key] = False
            else:
                self.__traits_dict[key] = True

    def check_trait(self, trait):
        return self.__traits_dict[trait]

    def check_name(self, guess):
        return guess == self.__traits_dict[guess]

    def get_trait(self, trait):
        return self.__traits_dict[trait]

    def __str__(self):
        return (self.__name)

    def __repr__(self):
        return self.__name.upper()

    def print_character(self):
        for key in self.__traits_dict:
            print("{} : {}".format(key, self.__traits_dict[key]))

##############END OF CHARACTER CLASS#################

import random

class Player:
    def __init__(self, player_name, list_of_characters):
        self.__list_of_characters = list_of_characters.copy() #list of opponents possible characters
        self.player_name = player_name
        total_characters = len(list_of_characters)
        random_index = random.randint(0, total_characters-1)
        self.__players_character = self.__list_of_characters[random_index]
        self.opponent = None
        self.__askable_traits = [
            "female", "facial_hair", "moustache", "beard", "black_hair", "ginger_hair",
            "brown_hair", "white_hair", "hair_partition", "curly_hair", "hat", "bald", "long_hair", "glasses",
            "earrings", "big_nose", "big_mouth", "red_cheeks", "blue_eyes", "sad"
        ]

        self.__win = False

    def set_opponent(self, player):
        self.opponent = player

    def get_players_character(self):
        return self.__players_character

    def get_characters(self):
        return self.__list_of_characters

    def set_win(self):
        self.__win = True

    def has_won(self):
        return self.__win

    def check_question(self, question):
        return self.__players_character.check_trait(question)

    def asks_random_question(self):
        size = len(self.__askable_traits)
        random_index = random.randint(0, size-1)
        question = self.__askable_traits[random_index]
        print("Is this a trait of your character? : {}".format(question.upper()))
        answer = self.opponent.check_question(question)
        print("{} responded : {}".format(self.opponent.player_name, answer))
        self.__askable_traits.pop(random_index) # removing question once asked.
        return (question, answer)

    def remove_characters(self, character_trait_tuple ):
        # character_trait is a tuple. It contains the character_trait that was guessed, and the answer
        # for example, if player1 guessed "does the character have blue eyes", it would receive a tuple
        # (blue_eyes, False) which would indicate that the opponents character does not have blue eyes.
        # based on this, all characters with blue eyes would be removed from the list_of_characters
        trait = character_trait_tuple[0]
        answer = character_trait_tuple[1]
        count = 0
        for i in range(len(self.__list_of_characters)-1, -1, -1):
            character = self.__list_of_characters[i]
            if character.check_trait(trait) != answer:
                self.__list_of_characters.pop(i)
                count += 1

        print("Removed {} characters".format(count))
        print("{} has {} possible characters remaining.".format(self.player_name, self.get_remaining_characters()))

        if len(self.__list_of_characters) == 1:
            self.set_win()

    def get_remaining_characters(self):
        return len(self.__list_of_characters)

######### END OF PLAYER CLASS ############

import csv

def get_characters_from_file():
    #get all the characters from the csv file
    #create character, add character to list of characters.
    #return this list of characters.
    character_list = []
    with open('guess_who_characters_x.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        row_count = 0
        for row in reader:
            row_count += 1
            if row_count == 1:
                continue
            new_character = Character(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7],
                row[8], row[9], row[10], row[11], row[12], row[13], row[14],
                row[15], row[16], row[17], row[18], row[19], row[20], row[21]
            )
            character_list.append(new_character)

        print("{} characters created.".format(len(character_list)))
        return character_list


def initialize_players(character_list):
    # create p1 and p2, give them both the list of characters
    player1 = Player("Player 1", character_list)
    player2 = Player("Player 2", character_list) # creating player 1 and 2 and giving them the characters
    player1.set_opponent(player2)
    player2.set_opponent(player1)

    return player1, player2

def run_game():
    list_of_characters = get_characters_from_file()
    player1, player2 = initialize_players(list_of_characters)

    while(player1.get_remaining_characters() != 1 and player2.get_remaining_characters() != 1):
        #ask questions
        print()
        print("Player 1's Turn: ")
        answer = player1.asks_random_question() # returns a tuple containing character trait and whether or not it is present
        player1.remove_characters(answer) #remove characters based on the answer
        if player1.has_won():
            print("**************************************")
            print("            PLAYER 1 WINS!")
            print("The opponent's character was: {}".format(player2.get_players_character()))
            print("**************************************")
            print()
            print() #only remaining character in character list
            return player1
            break
        print()
        print()

        print("Player 2's Turn: ")
        answer = player2.asks_random_question()
        player2.remove_characters(answer)
        if player2.has_won():
            print("**************************************")
            print("            PLAYER 2 WINS!")
            print("The opponent's character was: {}".format(player1.get_players_character()))
            print("**************************************")
            print()
            print()
            return player2
            break
        print()
    #End of run_game()

def main():
    player1_win_count = 0
    player2_win_count = 1
    i = 0
    while(i < 10000):
        victor = run_game()
        if victor.player_name == "Player 1":
            player1_win_count += 1
        else:
            player2_win_count += 1
        i += 1

    print("+++ SIMULATED 10000 GAMES +++")
    print("+ Player 1 won {} times   +".format(player1_win_count))
    print("+ Player 2 won {} times   +".format(player2_win_count))
    print("+++++++++++++++++++++++++++++")
    print()
    print("...")



main()
