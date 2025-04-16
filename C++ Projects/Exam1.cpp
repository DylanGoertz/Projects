// This program displays a meun and uses input to call specific functions
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
using namespace std;

// Functions
void calcAverage();
void calcMinimum();
void calcMaximum();
void writeFile(string fileName);
void readFile();

int main()
// Main function for menu
{
    int selection;

    do
    {
        // Menu
        cout << "1 - Calculate average\n";
        cout << "2 - Calculate minimum\n";
        cout << "3 - Calculate maximum\n";
        cout << "4 - Write data to a file\n";
        cout << "5 - Read data from a file\n";
        cout << "6 - Exit\n";
        cout << "Enter choice: "; 
        cin >> selection;

        switch (selection)
        // Switch operator to asign functions to each case
        {
            case 1:
            // Calculate average
            calcAverage();
            break;
            case 2:
            // Calculate and display the minimum value entered by the user
            calcMinimum();
            break;
            case 3:
            // Calculate and display the maximum value entered by the user
            calcMaximum();
            break;
            case 4:
            {
                // Get the filename from the user to write data to
                cout << "Enter the filename: \n";
                string fileName;
                cin >> fileName;
                writeFile(fileName); // Write user input to the specified file by calling function
                break;
            }
            break;
            case 5:
            // Read and display data from a user-specified file
            readFile();
            break;
            case 6:
            break;
            default:
            cout << "Not a valid choice, please try again!\n";
            break;
        }
    }
    // Input validation
    while (selection != 6);

    return 0;
}

void calcAverage()
// Function to give average of given integers from the user
{   
    int numIntegers;

    // User input to get the number of integers being used
    cout << "How many integers do you wish to enter?\n";
    cin >> numIntegers;
    // Input validation
    while (numIntegers <= 0)
    {
        cout << "Has to be a positive integer! Please try again.";
        cin >> numIntegers;
    }

    int sum = 0; // Inialize the sum to store all the integers entered from the user

    // For loop initalizer
    for (int i = 0; i < numIntegers; i++)
    {
        // Get number from user
        int value;
        cout << "Enter integer: " << (i + 1) << endl;
        cin >> value;
        sum += value; // Add current integer number to sum
    }

    // Calculate average
    int average = sum / numIntegers;
    cout << "The average is: " << average << endl;
}

void calcMinimum()
{
    int value, min;

    // Get first number from user
    cout << "Enter first number: \n";
    cin >> value;
    min = value; // This first number is the intial minimum

    // Keep getting numbers until user enters -99
    while(value != -99) 
    {
        cout << "Enter another number (-99 to stop): \n";
        cin >> value;

        // Update the minimum value if the current number is less than the current minimum and is not -99
        if(value != -99 && value < min) 
        {
            min = value;
        }
    }

    // Return the minimum value found
    cout << "The minimum value is: " << min << endl;
}

void calcMaximum() 
{
    int value, max;
    // Get first number from user
    cout << "Enter the first number: ";
    cin >> value;
    max = value; // This first number is the intial maximum

    // Using a do-while loop to ensure at least one number is entered
    do 
    {
        cout << "Enter another number (99 to stop): \n";
        cin >> value;

        // Update the maximum value if the current number is greater than the current maximum and is not 99
        if(value != 99 && value > max) 
        {
            max = value;
        }
    } 
    while(value != 99); // Keep getting numbers from the user until they enter 99

    // Display the maximum value to the user
    cout << "The maximum value is: " << max << endl;
}

void writeFile(string fileName) 
{
    // Create an output file stream with the specified filename
    ofstream out(fileName);

    // Check if the file opened successfully
    if(!out) 
    {
        cout << "Failed to open the file.\n";
        return;
    }

    // Get lines of text from the user until they type "STOP"
    cout << "Enter lines of text (type 'STOP' to end):\n";
    string line;
    cin.ignore(); // Clear any remaining input from the buffer
    while(getline(cin, line) && line != "STOP") 
    {
        out << line << endl; // Write the current line to the file
    }

    // Close the file after writing all the data
    out.close();
}

void readFile() 
{
    // Ask the user for the filename to read data from
    cout << "Enter the filename to read: \n";
    string fileName;
    cin >> fileName;

    // Create an input file stream with the specified filename
    ifstream in(fileName);

    // Check if the file can be opened
    while(!in) 
    {
        cout << "Cannot open the file. Enter a valid filename: \n";
        cin >> fileName;
        in.open(fileName); // Try to open the file again
    }

    // Read lines from the file and display them to the user
    cout << "Contents of the file:\n";
    string line;
    while(getline(in, line)) 
    {
        cout << line << endl;
    }

    // Close the file after reading all the data
    in.close();
}
