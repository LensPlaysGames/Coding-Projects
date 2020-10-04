/*
Title: Two-Digit-Prime-Factorization
Desc: My failed Solve at Problem 3 from Project Euler Archive

Project Euler Problem Desc:
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

CODE BY LENS
*/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<vector<unsigned long long>> get_factors(unsigned long long factor_me) {
    vector<vector<unsigned long long>> factors;

    factors.push_back(vector<unsigned long long> {factor_me, 1});

    unsigned long long i = factor_me - 1;
    while (i >= 2) {
        unsigned long long z = 2;
        while (z <= factor_me / 2 && z <= i) {
            if (i * z == factor_me) {
                vector<unsigned long long> f;
                f.push_back(i);
                f.push_back(z);
                factors.push_back(f);
            }
            z++;
        }
        i--;
    }

    return factors;
}

bool is_prime(unsigned long long check) {
    unsigned long long i = check - 1;
    while (i >= 2) {
        if (check % i == 0) {
            return false;
        }
        i--;
    }
    return true;
}

vector<unsigned long long> prime_factors(vector<vector<unsigned long long>> factors) {
    vector<unsigned long long> p_factors;

    for (size_t i = 0; i != factors.size(); i++)
    {
        for (size_t z = 0; z < factors[i].size(); z++)
        {
            if (is_prime(factors[i][z])) {
                p_factors = factors[i];
                continue;
            }
            else {
                p_factors = vector<unsigned long long>();
                break;
            }
        }

        if (!p_factors.empty()) {
            return p_factors;
        }
    }

    return p_factors;
}

unsigned long long largest_prime_factor(vector<vector<unsigned long long>> vec) {
    unsigned long long ans = 0;
    int n = vec.size() - 1;
    for (size_t i = n; i > 0; i--)
    {
        if (is_prime(vec[i][1])) {
            ans = vec[i][1];
            return ans;
        }
    }
    return ans;
}

void print_all(vector<unsigned long long> l) {
    cout << "\n(";
    for (size_t i = 0; i != l.size(); i++)
    {
        cout << l[i] << ((i == l.size() - 1) ? "" : ", ");
    }
    cout << ")\n\n";
}

void print_all_in_each(vector<vector<unsigned long long>> longs) {
    for (size_t i = 0; i != longs.size(); i++)
    {
        cout << "(";
        for (size_t z = 0; z < longs[i].size(); z++)
        {
            cout << longs[i][z] << ((z == longs[i].size() - 1) ? "" : ", ");
        }
        cout << ")\n";
    }
}

unsigned long long get_long_input() {
    unsigned long long i;
    cin >> i;
    while (true) {
        if (cin.fail()) {
            cout << "\n\nincorrect input, dawg\n\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cin >> i;
        }
        if (!cin.fail()) {
            if (i <= 2) {
                cout << "\n\ncan not get negative factors D:\n\n";
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                cin >> i;
                continue;
            }
            break;
        }
    }
    return i;
}

void loop() {
    cout << "\nEnter Number to Factorize\n";
    unsigned long long long_input = get_long_input();

    vector<vector<unsigned long long>> factors = get_factors(long_input);
    vector<unsigned long long> prime_facts = prime_factors(factors);

    unsigned long long large_prime = largest_prime_factor(factors);

    cout << "\nIs " << long_input << " Prime? " << ((is_prime(long_input)) ? "Yes" : "No") << "\n";
    cout << "\nFactors: \n";
    print_all_in_each(factors);
    cout << "\nPrime Factors: \n";
    print_all(prime_facts);

    cout << "The Largest Prime Factor Is: " << ((large_prime == 0) ? "No Prime Factors" : to_string(large_prime)) << "\n";

    loop();
}

int main() {
    cout << "Please Do Not Enter Numbers Above " << numeric_limits<unsigned long long>::max() << "\n";
    loop();
    return 0;
}