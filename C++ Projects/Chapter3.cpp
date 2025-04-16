// This program will ask for the principal, the annual interest rate, and the number of times the interest is compounded.
#include <iostream>
using namespace std;

int main()
{
    // Intializing variables
    float principal, annualInterest, finalBal, rate;
    int numberCompounded;

    // Taking input from user
    cout << "What is the principal?\n";
    cin >> principal;
    cout << "What is the annual interest rate?\n";
    cin >> annualInterest;
    cout << "Number of times interest compounded?\n";
    cin >> numberCompounded;

    // Initalzing the formulas
    rate = annualInterest / 100;
    finalBal = principal * ((pow((1 + rate / numberCompounded), numberCompounded)));

    // Outputing all of the info
    cout << "Interest Rate: " << annualInterest  << "%\n";
    cout << "Times Compounded: " << numberCompounded << endl;
    cout << "Principal: $" << principal << endl;
    cout << "Interest: $" << principal * ((pow((1 + rate / numberCompounded), numberCompounded))) - 1000 << endl;
    cout << "Final balance: " << finalBal << endl;
}