#include <stdlib.h>
#include <time.h>
#include <chrono>
#include <functional>
#include <iostream>
#include <string>
#include <unordered_map>
#include <Windows.h>
#include "termcolor.hpp"

#undef max

typedef void (*func_no_params)();

const int players = 2;
const char* PLAYS[3] = {
    "ROCK",
    "PAPER",
    "SCISSORS",
};

std::unordered_map<std::string, int> wins;

std::string get_winner(std::unordered_map<std::string, std::string> players) {
    // Draw Case
    if (players["0"] == players["1"]) {
        return "DRAW";
    }

    // Determine Who Won
    if (players["0"] == PLAYS[0]) { // Player 0 Played Rock
        if (players["1"] == PLAYS[1]) { // Player 1 Wins, Paper Covers Rock
            wins["P"] += 1; // Increment # of Wins with Paper
            return "1";
        }
        else if (players["1"] == PLAYS[2]) { // Player 0 Wins, Rock Smashes Scissors
            wins["R"] += 1; // Increment # of Wins with Rock
            return "0";
        }
    }
    else if (players["0"] == PLAYS[1]) { // Player 0 Played Paper
        if (players["1"] == PLAYS[0]) { // Player 0 Wins, Paper Covers Rocks
            wins["P"] += 1; // Increment # of Wins with Paper
            return "0";
        }
        else if (players["1"] == PLAYS[2]) { // Player 1 Wins, Scissors Cuts Paper
            wins["S"] += 1; // Increment # of Wins with Scissors
            return "1";
        }
    }
    else if (players["0"] == PLAYS[2]) { // Player 0 Played Scissors
        if (players["1"] == PLAYS[0]) { // Player 1 Wins, Rock Smashes Scissors
            wins["R"] += 1; // Increment # of Wins with Rock
            return "1";
        }
        else if (players["1"] == PLAYS[1]) { // Player 0 Wins, Scissors Cuts Paper
            wins["S"] += 1; // Increment # of Wins with Scissors
            return "0";
        }
    }

    return "ERROR";
}

void print_wins() {
    std::cout << "\n\n  ERRORS: " << wins["ERROR"] << "\n\n\n"
        << "Player Wins: \n"
        << "  - Player 0 Won " << ((wins["0"] > wins["1"] && wins["0"] > wins["DRAW"]) ? termcolor::on_green : termcolor::on_red) << wins["0"] << termcolor::reset << " Times\n"
        << "  - Player 1 Won " << ((wins["1"] > wins["0"] && wins["1"] > wins["DRAW"]) ? termcolor::on_green : termcolor::on_red) << wins["1"] << termcolor::reset << " Times\n"
        << "  - Drew/Tied " << ((wins["DRAW"] > wins["0"] && wins["DRAW"] > wins["1"]) ? termcolor::on_green : termcolor::on_red) << wins["DRAW"] << termcolor::reset << " Times\n"
        << ""
        << "\n\nAmount of Times a Winning Player Played: \n"
        << "  - Rock was Won with " << ((wins["R"] > wins["P"] && wins["R"] > wins["S"]) ? termcolor::on_green : termcolor::on_red) << wins["R"] << termcolor::reset << " Times\n"
        << "  - Paper was Won with " << ((wins["P"] > wins["R"] && wins["P"] > wins["S"]) ? termcolor::on_green : termcolor::on_red) << wins["P"] << termcolor::reset << " Times\n"
        << "  - Scissors was Won with " << ((wins["S"] > wins["R"] && wins["S"] > wins["P"]) ? termcolor::on_green : termcolor::on_red) << wins["S"] << termcolor::reset << " Times\n\n";
}

void simulate_game() {
    // Initialize "Dictionary" of players names and plays
    std::unordered_map<std::string, std::string> players;

    // Actually Generate a Play for each player
    players["0"] = PLAYS[rand() % 3];
    players["1"] = PLAYS[rand() % 3];
    std::string player_that_won = get_winner(players);
    wins[player_that_won] += 1;
}

void simulate_x_of_games(int x) {
    auto start = std::chrono::high_resolution_clock::now();
    int count = 0;
    for (int i = 0; i < x; i++) {
        simulate_game();
        count = i;
    }
    count++;
    auto stop = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);
    std::cout << "\n\n"
        << "Generated " << termcolor::green << count << termcolor::reset << " Games" << "\n"
        << "Time Elapsed: " << termcolor::green << elapsed.count() << termcolor::reset << "ms\n"
        << "\n";

}

int get_size_input() {
    int num_of_games = 0;
    std::cout << "How Many Games Would You Like to Simulate?\n";
    std::cin >> num_of_games;
    while (true) {
        if (std::cin.fail()) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "\nIncorrect Input. Integer Numbers Only!\n\n";
            std::cin >> num_of_games;
        }
        if (!std::cin.fail()) {
            break;
        }
    }


    return num_of_games;
}

void restart(func_no_params func) {
    std::cout << "\n\n"
        << "RESTARTING  RESTARTING  RESTARTING"
        << "\n\n\n\n";

    wins.clear();

    func();
}

int main() {
    srand(time(NULL));

    simulate_x_of_games(get_size_input());

    print_wins();

    restart((func_no_params)main);
}