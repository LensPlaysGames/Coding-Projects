"""
Title: Rock-Paper-Scissors-Simulation-and-Data
Desc: A Simple Python Console Application to Simulate Games of Rock, Paper, Scissors, and then Get Data From That and Plot it on a bar graph!

Credits:
CODE BY LENS
"""

import constants
import math
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

 # GLOBALS

count = 0
wins = [{}]

player_zero_last_play = ""
player_one_last_play = ""



 # FUNCTIONS

def startup_info():
    print(); print("WELCOME TO LensorRadii_Python_LotsOfRockPaperScissors")
    print("V0.1.0"); print()

def simulate_game():
    global player_zero_last_play
    global player_one_last_play

     # Get Random Play for each Player
    players = {}
    plays_length = len(constants.PLAYS)
    players["Player Zero"] = constants.PLAYS[np.random.randint(plays_length)]
    players["Player One"] = constants.PLAYS[np.random.randint(plays_length)]

     # Simulate Human Behaviour (no repeat)
    players = act_as_person(players)

     # Get the Winner and Add it to list of games won
    winner = get_winner(players)
    add_winner(winner)

    player_zero_last_play = players["Player Zero"]
    player_one_last_play = players["Player One"]

 # I would love to expand this section after playing some Rock, Paper, Scissors and paying attention to the avg person's strategy
def act_as_person(players):
    plays_length = len(constants.PLAYS)

     # Check Against Last Play as to not repeat Plays (Human Player Simulation)
    while players["Player Zero"] == player_zero_last_play:
        if np.random.randint(10) == 0: break
        players["Player Zero"] = constants.PLAYS[np.random.randint(plays_length)]

    while players["Player One"] == player_one_last_play:
        if np.random.randint(10) == 0: break
        players["Player One"] = constants.PLAYS[np.random.randint(plays_length)]

    return players

def get_winner(plays):
     # Draw/Tied Case
    if plays["Player Zero"] == plays["Player One"]:
        return "DRAW"
    else: # Determine Who Won
        if plays["Player Zero"] == constants.PLAYS[0]:
            if plays["Player One"] == constants.PLAYS[1]: # play2 beat play1 Paper Covers Rock
                return ("Player One", plays["Player One"])
            elif plays["Player One"] == constants.PLAYS[2]: # play1 beat play2 Rock Breaks Scissors
                return ("Player Zero", plays["Player Zero"])
        elif plays["Player Zero"] == constants.PLAYS[1]:
            if plays["Player One"] == constants.PLAYS[0]: # play1 beat play2 Paper Covers Rock
                return ("Player Zero", plays["Player Zero"])
            elif plays["Player One"] == constants.PLAYS[2]: # play2 beat play1 Scissors Cuts Paper
                return ("Player One", plays["Player One"])
        elif plays["Player Zero"] == constants.PLAYS[2]:
            if plays["Player One"] == constants.PLAYS[0]: # play2 beat play1 Rock Breaks Scissors D:
                return ("Player One", plays["Player One"])
            elif plays["Player One"] == constants.PLAYS[1]: # play1 beat play2 Scissors Cuts Paper
                return ("Player Zero", plays["Player Zero"])
    
     # Return Error if No Draw and No Winner was Found
    return ("ERROR", "Error Getting Winner.")

 # Add Winning Player and Winning Play to Dictionary of Game Wins
def add_winner(winner):
    if not isinstance(winner, tuple):
        return
    wins.append({"Player": winner[0], "Play": winner[1]})

def get_data():
    data = {}
    
    for k in wins:
         # Get # of Times each Player has Won
        if "Player" in k:
            data["Player Wins"] = Counter(k["Player"] for k in wins if k.get("Player"))
         # Get # of Times each Play ('ROCK', 'PAPER', 'SCISSORS') was Played by a Winning Player
        if "Play" in k:
            data["Winning Plays"] = Counter(k["Play"] for k in wins if k.get("Play"))

    return data


def print_data(data):
     # Print # of Times each Player has Won To Console
    print(); print("Player Stats: ")
    print("Player Zero Won: " + str(data["Player Wins"]["Player Zero"]) + " times")
    print("Player One Won: " + str(data["Player Wins"]["Player One"]) + " times"); print()

     # Print # of Times each Play was Played by a Winning Player To Console
    print(); print("# of Times Played: ")
    for p in range(len(constants.PLAYS)):
        print(constants.PLAYS[p] + ": " + str(data["Winning Plays"][constants.PLAYS[p]]))

 # Check if str is int
def check_digit(s):
    if len(s) != 0:
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()

def plot_data(data):
    global count

     # Initialize Data We are Going to Plot
    player_wins = dict(data["Player Wins"])
    wins_by_play = dict(data["Winning Plays"])

     # Number of Wins per Player
    wins_x = [] # Strings Containing Player Name
    wins_y = [] # Ints Containing # of Times Player has Won

     # Number of Winning Plays per Play Possibility
    plays_x = [] # Strings Containing Play ['ROCK', 'PAPER', 'SCISSORS']
    plays_y = [] # Ints Containing # of Times Play has been Played by a Winning Player

     # Convert Data to Format that MatPlotLib understands (list of 'str' or 'int')
    for w in player_wins: # For every dictionary in list, append key to x and value to y
        wins_x.append(str(w))
        wins_y.append(int(player_wins[w]))

    for p in wins_by_play: # For every dictionary in list, append key to x and value to y
        plays_x.append(str(p))
        plays_y.append(int(wins_by_play[p]))

     # Create Graph Figure
    fig, axs = plt.subplots(1, 2)
    fig.suptitle("Rock Paper Scissors Stats by Lens", fontsize=18)
    fig.tight_layout()

     # Fill in Graph Values
    axs[0].bar(wins_x, wins_y)
    axs[1].bar(plays_x, plays_y)

     # Label Each Bar Graph with It's Value
    for win_x in wins_x:
        axs[0].text(win_x, player_wins[win_x], str(player_wins[win_x]), ha="center", bbox=dict(fc="red", pad=1))

    for play_x in plays_x:
        axs[1].text(play_x, wins_by_play[play_x], str(wins_by_play[play_x]), ha="center", bbox=dict(fc="red", pad=1))

     # Label Plots
    axs[0].set_title("# of Wins per Player")
    axs[0].set_xlabel("Player")
    axs[0].set_ylabel("# of Wins")

    axs[1].set_title("# of Winning Plays per Play")
    axs[1].set_xlabel("Play")
    axs[1].set_ylabel("# of Times A Play was Won With")

     # Set Graph Scale
    axs[0].set_yticks(axs[0].get_yticks(), 5)
    axs[1].set_yticks(axs[0].get_yticks(), 5)

    for ax in range(len(axs)):
        axs[ax].spines["top"].set_visible(False)
        axs[ax].spines["right"].set_visible(False)

    plt.show()



 # MAIN PROGRAM

def main():
    global wins
    global count
    wins = [{}]
    count = 0

    startup_info()
    
    print("How Many Iterations to Test?")
    read = input()

    if check_digit(read):
        for i in range(int(read)):
            simulate_game()
            count = i
        count += 1
        print(); print("Simulated " + str(count) + " Games"); print()

        data = get_data()
        print_data(data)

        print(); print(); input("Press 'Enter' or 'Return' To Plot Data")

        plot_data(data)

        print(); print(); input("Press 'Enter' or 'Return' To Restart")

        main()
    else:
        print()
        print("INCORRECT INPUT FORMAT (Integer Only)")
        print()

        main()

main()
