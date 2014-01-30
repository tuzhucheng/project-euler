#include<iostream>

using namespace std;

int main()
{
    int n;
    int a = 3;
    int b = 5;
    int sum = 0;

    cout << "Enter a number and this program will output the sum of multiples of 3 or 5 below the number:\n";
    cin >> n;

    while (a < n) {
        sum += a;
        a += 3;
    }

    while (b < n) {
        if (b % 3 != 0)
            sum += b;
        b += 5;
    }

    cout << "The sum is " << sum << ".\n";     

    return 0;
}
