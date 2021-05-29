'''
Author: Advait Rao
Date: 26-05-2021
GuessWhoSimulator.py: This program runs simulations of the board game Guess Who.
'''
########################################################
# THIS CLASS CREATES A PERSON IN THE GAME OF GUESS WHO #
########################################################

# name (String)  : The first name of the person
# gender (String) : The person's gender
# facial_hair (String) : Mustache, Beard or NULL
# hair_color (String) : Black, Blonde, Red, Brown or NULL
# hair_length (String) : Short, Long or Bald
# hair_style : Straight or Curly
# glasses (boolean) : Does the person wear glasses?
# earrings (boolean) Does the person wear earrings?
# nose_size (String) : Small, Medium, Large
# red_cheeks (boolean) : Does the person have red cheeks?
# blue_eyes (boolean) : Does the person have blue eyes?
# sad (boolean) : Does the person look sad?


class Person:

    def __init__(self, name, gender, facial_hair, hair_color, hair_length,
    hair_style, glasses, earrings, nose_size, big_mouth, red_cheeks, blue_eyes, sad):
        self.__name = name
        self.__gender = gender
        self.__facial_hair = facial_hair
        self.__hair_color = hair_color
        self.__hair_length = hair_length
        self.__hair_style = hair_style
        self.__glasses = glasses
        self.__earrings = earrings
        self.__nose_size = nose_size
        self.__big_mouth = big_mouth
        self.__red_cheeks = red_cheeks
        self.__blue_eyes = blue_eyes
        self.__sad = sad
        print("Person ({}) created.".format(self.__name))

    def check_name(self, guess):
        return guess == self.__name

    def check_gender(self, guess):
        return guess == self.__gender

    def check_facial_hair(self, guess):
        return guess == self.__facial_hair

    def check_hair_color(self, guess):
        return guess == self.__hair_color

    def check_hair_length(self, guess):
        return guess == self.__hair_length

    def check_hair_style(self, guess):
        return guess == self.__hair_style

    def check_glasses(self, guess):
        return guess == self.__glasses

    def check_earrings(self, guess):
        return guess == self.__earrings

    def check_nose_size(self, guess):
        return guess == self.__nose_size

    def check_big_mouth(self, guess):
        return guess == self.__big_mouth

    def check_red_cheeks(self, guess):
        return guess == self.__red_cheeks

    def check_blue_eyes(self, guess):
        return guess == self.__blue_eyes

    def check_sad(self, guess):
        return guess == self.__sad

    def __str__(self):
        return "A man named {}".format(self.__name)

    def __repr__(self):
        return "[Person: {} ({})]".format(self.__name, self.__gender)



def main():
    new_person = Person("Advait", "M", "Mustache", "Black", "Short", "Straight", True, False, "Large", False, False, False)
    print(new_person)
    print(repr(new_person))

main()
