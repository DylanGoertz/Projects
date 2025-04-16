// This program uses arrays and functions to sort eight random integers 
#include <iostream>
#include <iomanip> 

using namespace std;

const int SIZE = 8;

// Function prototypes
void bubbleSort(int[], int);
void selectionSort(int[], int);
void showNums(int[], int);

int main()
{
    // Two identical arrays
    int array1[SIZE] = {705, 98, 221, 400, 50, 62, 120, 80};
    int array2[SIZE] = {705, 98, 221, 400, 50, 62, 120, 80};

    cout << "Original array 1: ";
    showNums(array1, SIZE);

    // Call function to sort the first array using bubble sort
    bubbleSort(array1, SIZE);

    cout << "Sorted array 1: ";
    showNums(array1, SIZE);

    cout << "Original array 2: ";
    showNums(array2, SIZE);

    // Call function to sort the second array using selection sort
    selectionSort(array2, SIZE);

    cout << "Sorted array 2: ";
    showNums(array2, SIZE);

    return 0;
}

void showNums(int array[], int numElts)
{
    // Display the array elements
    for (int pos = 0; pos < numElts; pos++)
        cout << setw(5) << array[pos];
    cout << endl;
}

void bubbleSort(int array[], int numElts)
{
    // Outer loop controls number of passes
    for (int pass = 0; pass < numElts - 1; pass++)
    {
        // Inner loop controls number of comparisons for each pass
        for (int index = 0; index < numElts - pass - 1; index++)
        {
            // Compare adjacent elements
            if (array[index] > array[index + 1])
            {
                // Swap elements
                int temp = array[index];
                array[index] = array[index + 1];
                array[index + 1] = temp;
            }
        }
        cout << "Pass " << pass + 1 << ": ";
        showNums(array, numElts);
    }
}

void selectionSort(int array[], int numElts)
{
    // Outer loop controls number of passes
    for (int startIdx = 0; startIdx < numElts - 1; startIdx++)
    {
        int minIdx = startIdx;

        // Inner loop controls number of comparisons for each pass
        for (int currentIdx = startIdx + 1; currentIdx < numElts; currentIdx++)
        {
            // Compare elements
            if (array[currentIdx] < array[minIdx])
                minIdx = currentIdx;
        }
        // Swap elements
        int temp = array[startIdx];
        array[startIdx] = array[minIdx];
        array[minIdx] = temp;

        cout << "Pass " << startIdx + 1 << ": ";
        showNums(array, numElts);
    }
}