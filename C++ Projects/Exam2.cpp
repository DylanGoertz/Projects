#include <iostream>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;

class Student 
{
private:
    string Name;
    int Age;
    double GPA;

public:
    // Default constructor
    Student() : Name(""), Age(0), GPA(0.0) {}

    // Non-default constructor
    Student(string name, int age, double gpa) : Name(name), Age(age), GPA(gpa) {}

    // Set/Get methods
    void setName(string name) 
    {
        Name = name;
    }

    string getName() const 
    {
        return Name;
    }

    void setAge(int age) 
    {
        Age = age;
    }

    int getAge() const 
    {
        return Age;
    }

    void setGPA(double gpa) 
    {
        GPA = gpa;
    }

    double getGPA() const 
    {
        return GPA;
    }

    // Display student information
    void displayStudent() const 
    {
        cout << "Name: " << Name << ", Age: " << Age << ", GPA: " << GPA << endl;
    }

    // Destructor
    ~Student() 
    {
        cout << "Student object for " << Name << " has been deleted." << endl;
    }
};

// Function protoypes
void bubbleSort(Student[], int);

// Function to accept student information
void acceptStudentInfo(Student * studentArr, int numStudents) 
{
    for (int i = 0; i < numStudents; i++) 
    {
        string name;
        int age;
        double gpa;

        cout << "Enter information for Student " << (i + 1) << ":" << endl;
        cout << "Name: ";
        cin >> name;
        cout << "Age: ";
        cin >> age;
        cout << "GPA: ";
        cin >> gpa;

        studentArr[i] = Student(name, age, gpa);
    }
}

// Function to display student information
void displayStudentInfo(Student * studentArr, int numStudents) 
{
    for (int i = 0; i < numStudents; i++) 
    {
        studentArr[i].displayStudent();
    }
}

// Function to sort students based on GPA in ascending order
void sortStudentGPA(Student studentArr[], int numStudents) 
{
    bool madeAswap = true;      // This allows the for loop to begin iterating

   for (int maxElement = numStudents - 1; maxElement > 0 && madeAswap; maxElement--)
   {  
      madeAswap = false;       // No swaps have occurred yet on this pass
      
      for (int index = 0; index < maxElement; index++)
      {
         if (studentArr[index].getGPA() > studentArr[index + 1].getGPA())
         {
             swap(studentArr[index], studentArr[index + 1]);
             madeAswap = true;
         }
      }
   } 
}

int main() 
{
    int numStudents;
    const int SIZE = numStudents;

    cout << "How many students to create: ";
    cin >> numStudents;

    Student * studentArr = new Student[numStudents];

    acceptStudentInfo(studentArr, numStudents);

    cout << "Student Information (Unsorted):" << endl;
    displayStudentInfo(studentArr, numStudents);

    cout << "Student Information (Sorted):" << endl;
    bubbleSort(studentArr, SIZE);

    cout << "Student Information (Sorted by GPA in ascending order):" << endl;
    displayStudentInfo(studentArr, numStudents);

    delete[] studentArr;

    return 0;
}