#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

void input(vector<double> &arr, const string &name)
{
	cout << "Enter " << name << ":" << endl;
	for (int i = 0; i < arr.size(); ++i)
	{
    	cin >> arr[i];
	}
}

double spi(vector<double> &credits, vector<double> &grades)
{
	double totalCredits = 0.0;
	double sum = 0.0;
	for (int i = 0; i < credits.size(); ++i)
	{
    	sum += grades[i] * credits[i];
    	totalCredits += credits[i];
	}
	if(totalCredits == 0) {
    	cout<<"Please provide the credits of each subject";
    	return -1;
	}
	return sum / totalCredits;
}

double cpi(vector<double> &spiArray, int N)
{
	double sum = 0.0;
	for (int i = 0; i < spiArray.size(); ++i)
	{
    	sum += spiArray[i];
	}
	return sum/N;
}

int main()
{
	int courses, sems;
	cout << "Enter number of courses in the semester: ";
	cin >> courses;
	if(courses == 0) {
    	cout<<"Enter the correct number of courses";
    	return 0;
	}
	vector<double> credits(courses), grades(courses);
	input(credits, "course credits");
	input(grades, "course grades");
	double SPI = spi(credits, grades);
	if(SPI == -1) {
	    return 0;
	}
	cout << "SPI: " << fixed << setprecision(2) << SPI << endl;
    
	cout << "Enter number of semesters: ";
	cin >> sems;
	vector<double> spiArray(sems), totalCredits(sems);
	cout << "Enter SPI values for each semester:" << endl;
	input(spiArray, "SPI values");
	double CPI = cpi(spiArray, sems);
	cout << "CPI: " << fixed << setprecision(2) << CPI << endl;
	return 0;
}
