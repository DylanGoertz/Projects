#include <iostream>
#include <string>
#include <cstdlib>  // Include cstdlib for rand() and srand()
#include <ctime>    // Include ctime for time()

using namespace std;

// Class representing a coin
class Coin
{
    private:
        string sideUp;

    public:
        // default constucter that determines the side of the coin 
        Coin()
        {
            int s = rand() % 2;
            if (s == 0)
            {
                sideUp = "heads";
            }
            else
            {
                sideUp = "tails";
            }
        }

        // void function named toss that simulates the tossing of the coin
        void toss()
        {
            int s = rand() % 2;
            if (s == 0)
            {
                sideUp = "heads";
            }
            else
            {
                sideUp = "tails";
            }
        }

    // function named getSideUp that returns the value of the sideUp member variable
    string getSideUp()
    {
        return sideUp;
    }
};

int main()
{
    srand(time(NULL)); // Seed the random number generator with the current time

    int headCount = 0;
    int totalToss = 20;
    Coin coin;

    cout << "Coins will be tossed " << totalToss << " times" << endl;
    cout << "Initial value on top: " << coin.getSideUp() << endl;

    // Loop to simulate coin tosses
    for (int i = 0; i < totalToss; i++)
    {
        coin.toss();
        string s = coin.getSideUp();
        cout << "Toss: " << s << endl;
        if (s.compare("heads") == 0)
        {
            headCount++;
        }
    }

    // Display the results
    cout << "Heads facing up: " << headCount << endl;
    cout << "Tails facing up: " << (totalToss - headCount) << endl;

    return 0;
}