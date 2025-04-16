// This program asks the user to enter a number of seconds then relates that number to either days, hours, or minutes
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    // Initlize the variables
    int day, hour, minute, seconds;
    float num_days, num_hours, num_minutes;

    day = 86400;
    hour = 3600;
    minute = 60;

    cout << "Enter a number of seconds: ";
    cin >> seconds; 

    if (seconds >= day)
    {
        num_days = seconds / day;
        cout << num_days << " days in " << seconds << " seconds.\n";
    }
    else if (seconds >= hour && seconds < day)
    {
        num_hours = seconds / hour;
        cout << num_hours << " hours in " << seconds << " seconds.\n";
    }
    else if (seconds >= minute && seconds < hour)
    {
        num_minutes = seconds / minute;
        cout << num_minutes << " minutes in " << seconds << " seconds.\n";
    }
    else if (seconds < minute)
    {
        cout << seconds << " seconds.\n";
    }
    return 0;
}