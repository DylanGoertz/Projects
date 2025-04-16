// This program is notes for chapter 3
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int x = 3;
    float y = 4.5;
    int z;
    float w;


    w = static_cast<float>(x) / 2;

    cout << w << endl;

    string firstName, lastName, fullName;
    string stars;
    int numStars;

    cout << "please enter your first name: ";
    getline(cin, firstName);

    cout << "Please enter your last name: ";
    getline(cin, lastName);

    fullName = firstName + " " + lastName;

    numStars = fullName.length();
    stars.assign(numStars, '*');

    cout << stars << endl << fullName << endl << stars << endl;

    return 0;
}