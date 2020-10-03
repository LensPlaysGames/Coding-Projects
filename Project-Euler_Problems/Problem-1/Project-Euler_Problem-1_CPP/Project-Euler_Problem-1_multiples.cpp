/*
Title: Project-Euler_Problem-1-multiples
Desc: Lens Solve of Problem One from Project Euler Archives

Project Euler Problem Desc: https://projecteuler.net/problem=1
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.

CODE BY LENS
*/

#include <vector>
#include <iostream>

using namespace std;

vector<int> multiples;

int find_sum_of_ints(vector<int> l) {
    int count = 0;
    for (auto i = l.begin(); i != l.end(); i++)
    {
        count += *i;
    }
    return count;
}

void print_ints_in_list(vector<int> l) {
    for (auto i = l.begin(); i != l.end(); i++)
    {
        cout << *i << "\n";
    }
}

int main() {
    for (int i = 0; i < 1000; i++)
    {
        if (i % 3 == 0 || i % 5 == 0) {
            multiples.push_back(i);
        }
    }
    print_ints_in_list(multiples);

    int sum = find_sum_of_ints(multiples);
    cout << "\nSum of All Multiples of 3 and 5 is " << sum << "\n";

    return 0;
}