// This program uses arrays to take data from a file and output the gross pay of employees 
#include <iostream>
#include <fstream>
using namespace std;

class Payroll
{
    private:
		double hours;
		double rate;

	public:
		Payroll()
		{
			hours = 0;
			rate = 0;
		}
		void setHour(double x)
		{
			hours = x;
		}
		void setRate(double y)
		{
			rate = y;
		}
		int getHour()
		{
			return hours;
		}
		double getRate()
		{
			return rate;
		}
		double pay()
		{
			return hours * rate;
		}
};

int main()
{
	Payroll workers[7];

	ifstream infile;
	infile.open("payroll.dat");

	for (int x = 0; x < 7; x++)
	{
		double hour;
		double rate;

		infile >> hour;
		infile >> rate;
		
		workers[x].setHour(hour);
		workers[x].setRate(rate);
	}

	infile.close();

	for (int x = 0; x < 7; x++)
	{
		cout << "The gross pay of employee " << x + 1 << " is $" << workers[x].pay() << endl;
	}

	return 0;
}