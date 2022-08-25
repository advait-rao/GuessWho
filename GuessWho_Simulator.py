"""
Author: Advait Rao
Date: 26-05-2021
GuessWhoSimulator.py: This program runs simulations of the board game Guess Who.
"""


class Character:
    def __init__(
        self,
        name,
        female,
        facial_hair,
        moustache,
        beard,
        black_hair,
        ginger_hair,
        blonde_hair,
        brown_hair,
        white_hair,
        hair_partition,
        curly_hair,
        hat,
        bald,
        long_hair,
        glasses,
        earrings,
        big_nose,
        big_mouth,
        red_cheeks,
        blue_eyes,
        sad,
    ):

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
            "sad": sad,
        }

        for key in self.__traits_dict:
            if self.__traits_dict[key] == "F":
                self.__traits_dict[key] = False
            else:
                self.__traits_dict[key] = True

    def check_trait(self, trait):
        return self.__traits_dict[trait]

    def __str__(self):
        return self.__name

    def __repr__(self):
        return self.__name.upper()


# END OF CHARACTER CLASS

import random


class Player:
    def __init__(self, player_name, list_of_characters):
        self.__list_of_characters = (
            list_of_characters.copy()
        )  # list of opponents possible characters
        self.greedy_questions = [
            "big_mouth",
            "facial_hair",
            "curly_hair",
            "hair_partition",
            "female",
            "glasses",
            "moustache",
            "blue_eyes",
            "red_cheeks",
            "big_nose",
            "blonde_hair",
            "brown_hair",
            "white_hair",
            "ginger_hair",
            "bald",
            "hat",
            "beard",
            "sad",
            "black_hair",
            "long_hair",
            "earringss",
        ]
        self.optimal_question_tree = [
            "big_mouth",
            "curly_hair",
            "black_hair",
            "long_hair",
            "ginger_hair",
            "hair_partition",
            "moustache",
            "bald",
            "blonde_hair",
            "earrings",
            "bald",
            "facial_hair",
            "white_hair",
            None,
            None,
            "hat",
            "glasses",
            "blue_eyes",
            None,
            None,
            None,
            None,
            None,
            "blonde_hair",
            "beard",
            "blue_eyes",
            "big_nose",
            None,
            None,
            None,
            None,
            None,
            "sad",
            "red_cheeks",
            "blue_eyes",
        ]
        self.optimal_tree_index = 0
        self.player_name = player_name
        total_characters = len(list_of_characters)
        random_index = random.randint(0, total_characters - 1)
        self.__players_character = self.__list_of_characters[random_index]
        self.opponent = None
        self.__askable_traits = [
            "female",
            "facial_hair",
            "moustache",
            "beard",
            "black_hair",
            "ginger_hair",
            "brown_hair",
            "white_hair",
            "hair_partition",
            "curly_hair",
            "hat",
            "bald",
            "long_hair",
            "glasses",
            "earrings",
            "big_nose",
            "big_mouth",
            "red_cheeks",
            "blue_eyes",
            "sad",
        ]

        self.__win = False

    def set_opponent(self, player):
        self.opponent = player

    def get_players_character(self):
        return self.__players_character

    def set_win(self):
        self.__win = True

    def has_won(self):
        return self.__win

    def check_question(self, question):
        return self.__players_character.check_trait(question)

    def check_bs_question(self, starting_letter):
        return str(self.__players_character)[0] >= starting_letter

    def asks_random_question(self):
        size = len(self.__askable_traits)
        random_index = random.randint(0, size - 1)
        question = self.__askable_traits[random_index]
        print("  Is this a trait of your character? : {}".format(question.upper()))
        answer = self.opponent.check_question(question)
        print("  {} responded : {}".format(self.opponent.player_name, answer))
        self.__askable_traits.pop(random_index)  # removing question once asked.
        return (question, answer)

    def asks_bs_question(
        self,
    ):  # does the starting letter of the name of your character start with / come after -
        mid_index = len(self.__list_of_characters) // 2
        starting_letter = str(self.__list_of_characters[mid_index])[
            0
        ]  # gets starting letter of the name
        answer = self.opponent.check_bs_question(starting_letter)
        print(
            '  Does your character\'s name start with or come after "{}" in the alphabet?'.format(
                str(self.__list_of_characters[mid_index])[0]
            )
        )
        print("  {} responded : {}".format(self.opponent.player_name, answer))
        if answer:
            self.__list_of_characters = self.__list_of_characters[mid_index:]
        else:
            self.__list_of_characters = self.__list_of_characters[:mid_index]

        print(
            "  {} has {} possible characters remaining.".format(
                self.player_name, len(self.__list_of_characters)
            )
        )
        print()
        if len(self.__list_of_characters) == 1:
            self.set_win()

    def asks_greedy_question(self):
        question = self.greedy_questions[0]
        print("  Is this a trait of your character? : {}".format(question.upper()))
        answer = self.opponent.check_question(question)
        self.greedy_questions = self.greedy_questions[1:]
        answer = self.opponent.check_question(question)
        print("  {} responded : {}".format(self.opponent.player_name, answer))
        return (question, answer)

    def asks_optimal_question(self):
        question = self.optimal_question_tree[self.optimal_tree_index]
        print("  Is this a trait of your character? : {}".format(question.upper()))
        answer = self.opponent.check_question(question)

        try:
            if answer:
                self.optimal_tree_index = (2 * self.optimal_tree_index) + 2
            else:
                self.optimal_tree_index = (2 * self.optimal_tree_index) + 1
            print("  {} responded : {}".format(self.opponent.player_name, answer))
            return (question, answer)

        except:
            print("  {} responded : {}".format(self.opponent.player_name, answer))
            return (question, answer)

    def remove_characters(self, character_trait_tuple):
        # character_trait is a tuple. It contains the character_trait that was guessed, and the answer
        # for example, if player1 guessed "does the character have blue eyes", it would receive a tuple
        # (blue_eyes, False) which would indicate that the opponents character does not have blue eyes.
        # based on this, all characters with blue eyes would be removed from the list_of_characters
        trait = character_trait_tuple[0]
        answer = character_trait_tuple[1]
        count = 0
        for i in range(len(self.__list_of_characters) - 1, -1, -1):
            character = self.__list_of_characters[i]
            if character.check_trait(trait) != answer:
                self.__list_of_characters.pop(i)
                count += 1

        print("  Removed {} characters".format(count))
        print(
            "  {} has {} possible characters remaining.".format(
                self.player_name, len(self.__list_of_characters)
            )
        )
        print()

        if len(self.__list_of_characters) == 1:
            self.set_win()

    def get_remaining_characters(self):
        return len(self.__list_of_characters)


# END OF PLAYER CLASS

import csv


def get_characters_from_file():
    # get all the characters from the csv file
    # create character, add character to list of characters.
    # return this list of characters.
    character_list = []
    with open("guess_who_characters_x.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        row_count = 0
        for row in reader:
            row_count += 1
            if row_count == 1:
                continue
            new_character = Character(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9],
                row[10],
                row[11],
                row[12],
                row[13],
                row[14],
                row[15],
                row[16],
                row[17],
                row[18],
                row[19],
                row[20],
                row[21],
            )
            character_list.append(new_character)

        print("  {} characters created.".format(len(character_list)))
        return character_list


def initialize_players(character_list, player1_name, player2_name):
    player1 = Player(player1_name, character_list)
    player2 = Player(
        player2_name, character_list
    )  # creating player 1 and 2 and giving them the characters
    player1.set_opponent(player2)
    player2.set_opponent(player1)

    return player1, player2


def players_turn(player):
    print("  {}'s Turn: ".format(player.player_name))
    if player.player_name in ["Player 1", "Player 2", "Naive Player"]:
        answer = (
            player.asks_random_question()
        )  # returns a tuple containing character trait and whether or not it is present
        player.remove_characters(answer)  # remove characters based on the answer

    if player.player_name == "BS Player":
        player.asks_bs_question()

    if player.player_name == "Greedy Player":
        answer = (
            player.asks_greedy_question()
        )  # returns a tuple containing character trait and whether or not it is present
        player.remove_characters(answer)  # remove characters based on the answer

    if player.player_name == "Optimal Player":
        answer = player.asks_optimal_question()
        player.remove_characters(answer)


def check_win(player1, player2):
    if player1.has_won():
        print_win_message(player1)
        return player1
    if player2.has_won():
        print_win_message(player2)
        return player2


def print_win_message(player):
    print("**************************************")
    print("          {} WINS!".format(player.player_name.upper()))
    print(
        "  The opponent's character was: {}".format(
            player.opponent.get_players_character()
        )
    )
    print("**************************************")
    print()
    print()


def begin_questioning(player_a, player_b):
    turns = 0
    while (
        player_a.get_remaining_characters() != 1
        and player_b.get_remaining_characters() != 1
    ):
        turns += 1
        print("  TURN {}".format(turns))
        players_turn(player_a)
        result = check_win(player_a, player_b)
        if result != None:
            return result

        players_turn(player_b)
        result = check_win(player_a, player_b)
        if result != None:
            return result


def run_game():
    list_of_characters = get_characters_from_file()
    player1, player2 = initialize_players(list_of_characters, "Player 1", "Player 2")
    # print("Player 1's character: {}".format(player1.get_players_character()))
    # print("Player 2's character: {}".format(player2.get_players_character()))
    i = random.randint(0, 1)
    if i == 1:  # player1 starts first
        result = begin_questioning(player1, player2)
        if result != None:
            return result
    else:  # player2 starts first
        result = begin_questioning(player2, player1)
        if result != None:
            return result
    # End of run_game()


def run_bs_game():  # Player1 uses the binary search strategy.
    list_of_characters = get_characters_from_file()
    bs_player, naive_player = initialize_players(
        list_of_characters, "BS Player", "Naive Player"
    )
    # print("BS Player's character: {}".format(bs_player.get_players_character()))
    # print("Naive Player's character: {}".format(naive_player.get_players_character()))
    i = random.randint(0, 1)
    if i == 1:  # bs_player starts first
        result = begin_questioning(bs_player, naive_player)
        if result != None:
            return result
    else:  # reg_player starts first
        result = begin_questioning(naive_player, bs_player)
        if result != None:
            return result


def run_greedy_game():
    list_of_characters = get_characters_from_file()
    greedy_player, naive_player = initialize_players(
        list_of_characters, "Greedy Player", "Naive Player"
    )
    # print("Greedy Player's character: {}".format(greedy_player.get_players_character()))
    # print("Naive Player's character: {}".format(naive_player.get_players_character()))
    i = random.randint(0, 1)
    if i == 1:  # greedy_player starts first
        result = begin_questioning(greedy_player, naive_player)
        if result != None:
            return result
    else:  # reg_player starts first
        result = begin_questioning(naive_player, greedy_player)
        if result != None:
            return result


def run_optimal_game():
    list_of_characters = get_characters_from_file()
    optimal_player, naive_player = initialize_players(
        list_of_characters, "Optimal Player", "Naive Player"
    )
    # print("Optimal Player's character: {}".format(optimal_player.get_players_character()))
    # print("Naive Player's character: {}".format(naive_player.get_players_character()))
    i = random.randint(0, 1)
    if i == 1:  # greedy_player starts first
        result = begin_questioning(optimal_player, naive_player)
        if result != None:
            return result
    else:  # reg_player starts first
        result = begin_questioning(naive_player, optimal_player)
        if result != None:
            return result


def run_optimal_v_greedy_game():
    list_of_characters = get_characters_from_file()
    optimal_player, greedy_player = initialize_players(
        list_of_characters, "Optimal Player", "Greedy Player"
    )
    # print("Optimal Player's character: {}".format(optimal_player.get_players_character()))
    # print("Greedy Player's character: {}".format(greedy_player.get_players_character()))
    i = random.randint(0, 1)
    if i == 1:  # greedy_player starts first
        result = begin_questioning(optimal_player, greedy_player)
        if result != None:
            return result
    else:  # reg_player starts first
        result = begin_questioning(greedy_player, optimal_player)
        if result != None:
            return result


def run_optimal_v_bs_game():
    list_of_characters = get_characters_from_file()
    optimal_player, bs_player = initialize_players(
        list_of_characters, "Optimal Player", "BS Player"
    )
    # print("Optimal Player's character: {}".format(optimal_player.get_players_character()))
    # print("BS Player's character: {}".format(bs_player.get_players_character()))
    i = random.randint(0, 1)
    if i == 1:  # greedy_player starts first
        result = begin_questioning(optimal_player, bs_player)
        if result != None:
            return result
    else:  # reg_player starts first
        result = begin_questioning(bs_player, optimal_player)
        if result != None:
            return result


def run_greedy_v_bs_game():
    list_of_characters = get_characters_from_file()
    greedy_player, bs_player = initialize_players(
        list_of_characters, "Greedy Player", "BS Player"
    )
    # print("Greedy Player's character: {}".format(greedy_player.get_players_character()))
    # print("BS Player's character: {}".format(bs_player.get_players_character()))
    i = random.randint(0, 1)
    if i == 1:  # greedy_player starts first
        result = begin_questioning(greedy_player, bs_player)
        if result != None:
            return result
    else:  # reg_player starts first
        result = begin_questioning(bs_player, greedy_player)
        if result != None:
            return result


def main():
    print("--------------------------------------------------------")
    print("                   GUESS WHO? SIMULATOR")
    print("--------------------------------------------------------")
    print("   Naive Strategy ..............................: 1")
    print("   Greedy Strategy .............................: 2")
    print("   Binary Search Strategy ......................: 3")
    print("   Optimal Strategy ............................: 4")
    print("   Optimal Strategy vs Greedy Strategy .........: 5")
    print("   Optimal Strategy vs Binary Search Strategy ..: 6")
    print("   Greedy Strategy vs Binary Search Strategy ...: 7")
    print("--------------------------------------------------------")
    print()
    strategy = int(input("   Enter your choice of strategy: "))
    simulations = int(input("   Enter the number of simulations to be run: "))
    print()
    player1_win_count = 0
    player2_win_count = 0
    i = 0
    while i < simulations:
        print("GAME {}:".format(i+1))
        print()
        if strategy == 1:
            victor = run_game()
            if victor.player_name == "Player 1":
                player1_win_count += 1
            else:
                player2_win_count += 1

        if strategy == 2:
            victor = run_greedy_game()
            if victor.player_name == "Greedy Player":
                player1_win_count += 1
            else:
                player2_win_count += 1

        if strategy == 3:
            victor = run_bs_game()
            if victor.player_name == "BS Player":
                player1_win_count += 1
            else:
                player2_win_count += 1

        if strategy == 4:
            victor = run_optimal_game()
            if victor.player_name == "Optimal Player":
                player1_win_count += 1
            else:
                player2_win_count += 1

        if strategy == 5:
            victor = run_optimal_v_greedy_game()
            if victor.player_name == "Optimal Player":
                player1_win_count += 1
            else:
                player2_win_count += 1

        if strategy == 6:
            victor = run_optimal_v_bs_game()
            if victor.player_name == "Optimal Player":
                player1_win_count += 1
            else:
                player2_win_count += 1

        if strategy == 7:
            victor = run_greedy_v_bs_game()
            if victor.player_name == "Greedy Player":
                player1_win_count += 1
            else:
                player2_win_count += 1

        i += 1

    player1_win_percentage = (
        player1_win_count / (player1_win_count + player2_win_count) * 100
    )
    player2_win_percentage = (
        player2_win_count / (player1_win_count + player2_win_count) * 100
    )

    print("**************************************")
    print("  SIMULATED {} GAMES".format(simulations))
    print()
    if strategy == 1:
        print("  Player 1 : Naive Strategy")
        print("  Player 2 : Naive Strategy")
        print()
    if strategy == 2:
        print("  Player 1 : Greedy Strategy")
        print("  Player 2 : Naive Strategy")
        print()
    if strategy == 3:
        print("  Player 1 : Binary Search Strategy")
        print("  Player 2 : Naive Strategy")
        print()
    if strategy == 4:
        print("  Player 1 : Optimal Strategy")
        print("  Player 2 : Naive Strategy")
        print()
    if strategy == 5:
        print("  Player 1 : Optimal Strategy")
        print("  Player 2 : Greedy Strategy")
        print()
    if strategy == 6:
        print("  Player 1 : Optimal Strategy")
        print("  Player 2 : Binary Search Strategy")
        print()
    if strategy == 7:
        print("  Player 1 : Greedy Strategy")
        print("  Player 2 : Binary Search Strategy")
        print()
    print(
        "  Player 1 won {} times ({:.2f}%) ".format(
            player1_win_count, player1_win_percentage
        )
    )
    print(
        "  Player 2 won {} times ({:.2f}%) ".format(
            player2_win_count, player2_win_percentage
        )
    )
    print("**************************************")
    print()
    print("...")


main()
