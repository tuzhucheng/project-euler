#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

struct power
{
    int base;
    int exponent;
};

// assuming n is positive integer
vector<power> factor(int n)
{
    vector<power> expanded;
    const int MAX = n;
    int powerMatrix[2][MAX];

    // initialize powerMatrix
    for (int i = 0; i < MAX; i++) {
        powerMatrix[0][i] = i+1;
        powerMatrix[1][i] = 0;
    }

    // factor
    for (int i = 2; i <= n; i++) {
        if (n % i == 0) {
            powerMatrix[1][i-1]++;
            n /= i;
            i--;
        }
    }

    // convert powerMatrix to vector<power>
    for (int i = 0; i < MAX; i++) {
        power newPower;
        newPower.base = powerMatrix[0][i];
        newPower.exponent = powerMatrix[1][i];
        expanded.push_back(newPower);
    }

    if (expanded.size() == 0) {
        power newPower;
        newPower.base = 1;
        newPower.exponent = 0;
        expanded.push_back(newPower);
    }

    return expanded;
}

void printPower(vector<power> expanded)
{
    bool first = true;

    if (expanded.size() == 1) {
        cout << expanded.at(0).base << "^" << expanded.at(0).exponent;
    }

    for (int i = 0; i < expanded.size(); i++)
    {
        if (expanded.at(i).exponent != 0) {
            if (!first) {
                cout << " * ";
            }
            first = false;
            cout << expanded.at(i).base << "^" << expanded.at(i).exponent;
        }
    }
    cout << endl;
}

int main()
{
    // Test for factor
    /*
    for (int i = 1; i < 11; i++) {
        vector<power> expanded = factor(i);
        printPower(expanded); 
    }
    */
    int smallest = 1;
    const int goesTo = 20;
    vector<power> lowestPowers;
    for (int i = 0; i < goesTo; i++) {
        power p;
        p.base = i+1;
        p.exponent = 0;
        lowestPowers.push_back(p);
    }

    for (int i = 1; i < goesTo; i++) {
        vector<power> expanded = factor(i);
        for (int j = 0; j < expanded.size(); j++) {
            if (expanded.at(j).exponent > lowestPowers.at(j).exponent) {
                lowestPowers.at(j).exponent = expanded.at(j).exponent;
            }
        }
    }
    
    for (int i = 0; i < lowestPowers.size(); i++) {
        smallest *= pow(lowestPowers.at(i).base, lowestPowers.at(i).exponent);
    }

    cout << "Smallest positive number that's evenly divisible by all numbers from 1 to " << goesTo << " is " << smallest << ".\n";
    printPower(lowestPowers);

    return 0;
}

