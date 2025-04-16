// This program 
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int num;
    num = 8;
    cout << --num << " ";
    cout << num++ << " ";
    cout << num << endl;

    int count = 1;

    while (count <= 5)
    {
        cout << "Hello   ";
        count = count + 1;
    }
    cout << "\nThat's all!\n";

    return 0;
}