#include<iostream>

using namespace std;

int sum(int a, int b, int n, int max)
{
    if (a+b > max)
        return n;
    else {
        int temp = a;
        a = b;
        b = temp + a;
        if (b % 2 == 0)
            n += b;
        return sum(a, b, n, max);
    }
}

int main()
{
    cout << "Sum of even-valued terms below 4 million is: " << sum(1,2,2,4000000) << endl;
    return 0;
}
