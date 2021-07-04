# GuessWho_Simulator.py
This project determines the best way to play the game **[Guess Who?](https://en.wikipedia.org/wiki/Guess_Who%3F)**

## Introduction
_Guess Who?_ is a board game in which the objective is to guess the opponent's character. Each player picks a character from a group of 24 characters, and then take turns asking yes or no questions, until one of them guesses the opponent's character.

In this project, 3 different strategies are tested, by simulating games of _Guess Who?_ and having different strategies face off against each other.


### The Strategies:
#### 1. The Naive Strategy
This strategy is the one adopted by most people playing the game. There is no logic or foresight involved, and questions are asked randomly.

#### 2. The Greedy Strategy
This strategy involves asking questions based on the expected number of characters left after asking the question. This is calculated by obtaining the sum of the product of the probability of a character having a certain trait and the number of characters with that trait and the product of the probability of a character not having that trait and the number of characters who do not have that trait.

For example, for the question "Does your character wear Ear rings?", the expected number of players left would be:

![Screenshot 2021-07-04 at 9 22 28 PM](https://user-images.githubusercontent.com/84999187/124380152-54affe00-dd0f-11eb-97d3-04ce8b883edd.png)


The _Greedy_ Strategy always asks the questions with the lowest Expected Number of Remaining Players metric.

This strategy is called The _Greedy_ Strategy because it makes the best choice for a single turn, while disregarding future options. The lack of foresight prevents this strategy from being too successful.

#### 3. The Optimal Strategy
The _Optimal_ Strategy takes from the _Greedy_ strategy, by asking questions that would result in the fewest remaining characters, and also maintains a Tree that stores the fastest route to victory from every possible scenario, when the Player's first question is "Does your character have a big mouth?". This question is the best question to ask in terms of the expected remaining players.

#### 4. The Binary Search Strategy
The Binary Search Strategy is based on  repeatedly asking a question that halves the expected remaining players. This is done by asking questions like "Does the first letter of your character's name come after H in the alphabet?".\
Since there are 24 possible characters to begin with, using this strategy, a Player can win in at most 5 turns.\
While this strategy technically doesn't break any rules of the game, it is definitely not the way the game was meant to be played.

## How it Works

The code for this project was written in Python 3.

All the character information is stored in a csv file `guess_who_characters_x.csv`

The program receives the number of games to be simulated and the strategy to be applied from the user.

When a game is simulated, the program reads the csv file and creates a list of `Character` objects. It then initialises two `Player` objects, based on the strategy selected in the menu. After each `Player` is given a secret character which must be guessed by their opponent, the program begins alternating between players so that they can each ask a question to their opponent.

**The program randomly decides which player gets the first turn**. This is important, as the player who starts typically has a 5% higher chance of winning, when playing the _Naive_ and _Greedy_ strategies. However, when playing the _Optimal_ and _Binary Search_ Strategy, this chance increases significantly.

Each Player maintains a list of characters `self.__list_of_characters` which contains all the characters that the opponent _could_ have. Based on responses to the Player's questions, Characters are removed from this list.

When only one `Character` remains in the list, i.e. the opponent's possible characters is narrowed down to one character, the game ends. The first player to narrow down their list to  to one `Character` is the winner.

The given number of games of _Guess Who?_ are simulated, and each Player's wins are counted. The program displays the results.

## Screenshots
The menu upon starting the program:

![download](https://user-images.githubusercontent.com/84999187/124383628-98abfe80-dd21-11eb-84f0-3661a5300b68.png)

The result at the end of execution:

![download (1)](https://user-images.githubusercontent.com/84999187/124383672-cc872400-dd21-11eb-99f4-d493f762a288.png)

How a game of _Guess Who?_ is represented:

![download (2)](https://user-images.githubusercontent.com/84999187/124383711-0ce6a200-dd22-11eb-808d-12654dd136a3.png)

## Conclusion
The Binary Search Strategy is found to be the most effective, beating the second best - The _Optimal_ Strategy - 60% of the time.

Since the Binary Search strategy could be construed as illegal, the _Optimal_ Strategy is the most recommended, beating the _Greedy_ and _Naive_ strategies roughly 85% of the time.

Being a highly random game, the only way to _really_ win a game of _Guess Who?_ every single time is to know the opponents character. However, if the situation ever arises where one has to play a game of _Guess Who?_ for their life, then adopting one of the aforementioned strategies may not be such a bad idea :)

#### Other Links

- A [youtube video](https://www.youtube.com/watch?v=FRlbNOno5VA&ab_channel=MarkRober) by Mark Rober. His strategy is essentially the same as the Binary Search Strategy, however his questions are different. He eliminates half the possible characters by combining questions, for example, "Does your character have Black hair **or** Blue Eyes **or** a big nose?"

- An [article](https://chalkdustmagazine.com/blog/cracking-guess-board-game/) by Rafael Prieto Curiel. This article brushes over Decision Theory and led me to the _Optimal_ Strategy.
