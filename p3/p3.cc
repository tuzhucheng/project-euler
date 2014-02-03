#include <iostream>
#include <math.h>

using namespace std;

const long input = 600851475143;

bool isPrime(int n)
{
    if (n <= 1) {
        return false;
    }

    int d = 2;
    int rt = sqrt(n);
    while (d <= rt) {
        if (n % d == 0) {
            return false;
        }
        d++;
    }
    return true;
}

int main()
{
    int divisor = sqrt(input);
    while (divisor > 1) {
        if (input % divisor == 0 && isPrime(divisor)) {
            cout << "The largest prime factor is " << divisor << ".\n";
            break;
        }
        divisor--;
    }

    return 0;
}
