// This program reads input from a file with a month name, an ending month name, and then the monthly rainfall for each month furing that period.
// Throughout the program it will sum the rainfall amounts and then report the total rainfall and avergare rainfall for that period.
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
    ifstream inputFile;
    string startName, endName;
    double value, total = 0.0, avg, c = 0.0;

    // opens file
    inputFile.open("rainfall.txt");

    inputFile >> startName;

    inputFile >> endName;

    if(!inputFile)
    {
        cout << "rainfall.txt file does not exsist in folder" << endl;
    }

    // Loop until EOF is reached
    while (inputFile >> value)
    {   
        total = total + value;
        c++;
    }
    avg = total/c;
    inputFile.close();
    cout << "\nDuring the months " << startName << "-" << endName << ", the total rainfall was " << total << " inches and the average monthly rainfall was " 
    << fixed << setprecision(2) << avg << " inches." << endl;

    return 0;

}