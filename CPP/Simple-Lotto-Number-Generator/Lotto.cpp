/*
Title: Simple-Lottery-Number-Generator
Desc: Generates Valid Hit-5 (WA Lottery) Numbers and Writes Them to "numbahz-yo.json" in JSON format

CODE BY LENS
*/

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <array>
#include <time.h>
#include <chrono>
#include <string>
#include <vector>
#include <set>
#include <unordered_set>
#include "json.hpp"

using namespace std;

typedef chrono::high_resolution_clock high_res_clock;
typedef nlohmann::json json;

array<int, 42> numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9,
    10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
    30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
    40, 41, 42 };

void display_startup_info() {
    cout << "\n"
        << "Lens' Lil Lottery Number Generator"
        << "\n";
}

auto get_duration(high_res_clock::time_point start, high_res_clock::time_point stop) {
    return (chrono::duration_cast<chrono::milliseconds>(stop - start)).count();
}

int generate_num(int last_num) {
    int number = 1;
    while (number <= last_num) {
        number = numbers[rand() % 42];
    }
    return number;
}

array<int, 5> generate_lotto_num() {
    array<int, 5> nums = {};
    int last_num = 1;
    for (int s = 0; s < 5; s++)
    {
        nums[s] = generate_num(last_num);
        if (nums[s] >= 42 - abs(s - 5)) {
            --s;
            last_num = ((s >= 0) ? nums[s] : 1);
            continue;
        }
        last_num = nums[s];
    }
    return nums;
}

vector<array<int, 5>> numbahz;

void write_numbahz_to_file() {
    ofstream file;
    file.open(("numbahz-yo.json"), ios_base::app);

    json output;
    unordered_map<string, array<int, 5>> o;
    for (size_t i = 0; i < numbahz.size(); i++)
    {
        o[to_string(i)] = numbahz[i];
    }
    output += o;

    file << setw(4) << output;
    file.close();
}

void get_x_lotto_nums(int x) {
    cout << "Starting Timer";
    auto start = high_res_clock::now();
    int count = 0;
    for (int i = 0; i < x; i++)
    {
        array<int, 5> lotto_num = generate_lotto_num();
        numbahz.push_back(lotto_num);
        count = i;
    }
    auto stop = high_res_clock::now();
    count += 1;
    cout << "\n\nGenerated " << count << " Numbers!\n"
        << "Time Elapsed: " << get_duration(start, stop) << "ms\n";
}

int get_int_input() {
    int z;
    cout << "\n\nENTER NUMBER OF VALID LOTTERY NUMBERS TO GENERATE\n\n";
    cin >> z;
    while (true) {
        if (cin.fail()) {
            cout << "\n\n   ERROR GETTING INPUT.    \n    INTEGERS ONLY!    \n\n";
            cin >> z;
        }
        else if (!cin.fail()) {
            break;
        }
    }
    return z;
}

void loop() {
    int x = get_int_input();
    get_x_lotto_nums(x);
    write_numbahz_to_file();
    loop();
}

int main() {
    srand((unsigned)time(0));

    loop();

    return 0;
}