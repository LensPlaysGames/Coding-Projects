/*
Title: Largest-Palindrome
Desc: My Solve of Problem 4 from Project Euler Archive

Project Euler Problem Desc: https://projecteuler.net/problem=4
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

CODE BY LENS
*/

#include <iostream>
#include <string>
#include <chrono>

using namespace std;
using namespace chrono;
// CONSTANTS
const int three_digit_min = 100;
const int three_digit_max = 999;

bool is_palindrome(string str) {
    string rev_str = str;
    reverse(rev_str.begin(), rev_str.end());
    if (str == rev_str) {
        return true;
    }
    return false;
}

int main() {
    auto start = high_resolution_clock::now();
    bool should_break = false;
    for (int x = three_digit_max; x >= three_digit_min; --x) {
        if (should_break) { break; }
        for (int y = three_digit_max; y >= three_digit_min; --y) {
            if (should_break) { break; }
            long product = x * y;
            if (is_palindrome(to_string(product))) {
                cout << "\n\n\nLargest Palindromic Product of Three Digit Numbers is " << to_string(product) << "\n\n\n";
                should_break = true;
            }
        }
    }
    auto stop = high_resolution_clock::now();
    auto elapsed_ms = duration_cast<milliseconds>(stop - start);
    auto elapsed_microseconds = duration_cast<microseconds>(stop - start);
    auto elapsed_nanoseconds = duration_cast<nanoseconds>(stop - start);

    cout << "Time Elapsed is " << elapsed_ms.count() << "ms\n"
        << "Microseconds Elapsed is " << elapsed_microseconds.count() << " microseconds\n"
        << "Nanoseconds Elapsed is " << elapsed_nanoseconds.count() << "ns\n";

    return 0;
}