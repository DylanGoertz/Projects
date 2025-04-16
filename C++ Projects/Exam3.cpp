#include <iostream>
#include <string>

using namespace std;

// Automobile class
class Automobile {
private:
    // Model, year, and milage private attributes
    string model;
    int year;
    double mileage;

public:
    // defualt constructor 
    Automobile() : model(), year(0), mileage(0.0) {}
    // non-defualt constructor 
    Automobile(string model, int year, double m) : model (model), year(year), mileage(m) {}

    // set and get methods for the attributes
    void setModel(string model) {model = model; }
    string getModel() const { return model; }

    void setYear(int year) { year = year; }
    int getYear() const { return year; }

    void setMileage(double m) { mileage = m; }
    double getMileage() const { return mileage; }

    // displayAuto will print the info from Automobile with all three atributes 
    void displayAuto() const {
        cout << "Model: " << model << ", Year: " << year << ", Mileage: " << mileage << endl;
    }

    // destructor
    ~Automobile() {
        cout << "Automobile object deleted" << endl;
    }
};

// inventory class
class Inventory {
// count, maxCount, and autoPtr private attributes
private:
    int count;
    int maxCount;
    Automobile *autoPtr;

public:
    // defualt constructor
    Inventory() : count(0), maxCount(10), autoPtr(nullptr) {}

    // non-defualt constructor 
    Inventory(int max) : count(0), maxCount(max) {
        autoPtr = new Automobile[maxCount];
    }

    // this will append a new automobile to the inventory and will not exceed the capacity of the inventory
    void addAutomobile(const Automobile &autoObj) {
        if (count < maxCount) {
            autoPtr[count] = autoObj;
            count++;
            cout << "Automobile added to inventory" << endl;
        } else {
            cout << "Inventory full! Cannot add more automobiles." << endl;
        }
    }

    // this will call displayAuto to display the current inventory
    void displayInventory() const {
        for (int i = 0; i < count; ++i) {
            autoPtr[i].displayAuto();
        }
    }

    // this will allow the user to search the inventory of cars below a given milage 
    void searchAuto(double mileage) const {
        cout << "Automobiles with mileage below " << mileage << ":" << endl;
        for (int i = 0; i < count; ++i) {
            if (autoPtr[i].getMileage() < mileage) {
                autoPtr[i].displayAuto();
            }
        }
    }

    // destructor 
    ~Inventory() {
        delete[] autoPtr;
        cout << "Destructor of Inventory class called" << endl;
    }
};

// This function will take the Inventory object as a parameter and then call the addAutomobile method to add the new car
void addNewAuto(Inventory &inv) {
    string model;
    int year;
    double mileage;
    cout << "Enter model: ";
    cin >> model;
    cout << "Enter year: ";
    cin >> year;
    cout << "Enter mileage: ";
    cin >> mileage;

    Automobile newAuto(model, year, mileage);
    inv.addAutomobile(newAuto);
}

// This function will take the Inventory object as a parameter and then ask the user for the mileage
// Then it will display all automobiles in the inventory below that mileage
void searchAuto(Inventory &inv) {
    double mileage;
    cout << "Enter maximum mileage: ";
    cin >> mileage;

    inv.searchAuto(mileage);
}

int main() {
    int numAutos;
    // asking user how many automobiles to create
    cout << "Enter the number of automobiles to create: ";
    cin >> numAutos;

    // inventory object to call the non-default constructor for that object with the number of automobiles given by the user
    Inventory inventory(numAutos);

    int choice;
    // using a do...while loop to display the menu 
    do {
        cout << "\nMenu:\n1: Add an automobile to the inventory\n2: Display the content of the inventory\n3: Display the automobiles below certain mileage\n4: Exit\nEnter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                addNewAuto(inventory);
                break;
            case 2:
                inventory.displayInventory();
                break;
            case 3:
                searchAuto(inventory);
                break;
            // goodbye message! 
            case 4:
                cout << "Thank you for shopping with us. Goodbye!" << endl;
                break;
            default:
                cout << "Invalid choice. Please enter a valid option (1-4)." << endl;
        }
    // making sure the user only inputs 1-4
    } while (choice != 4);

    return 0;
}