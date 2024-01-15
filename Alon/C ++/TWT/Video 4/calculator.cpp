#include <iostream>
#include <string> 
using namespace std;

// // const int gravity = -9.8;
    // int n;
    // cin >> n;
    // cin.clear();
    // cin.ignore(9999, '\n');
    // // Shows if there is a failure with input
    // cout << cin.fail();
    // // Clear removes error from the stream, ignore actually clears the value with the amount of chars you want to ignore

int main() {
    int num1, num2;
    cout << "Enter a number: ";
    cin >> num1;
    cin.clear();
    cin.ignore(9999, '\n');
    cout << "Enter another number: ";
    cin >> num2;
    int sum = num1 + num2;
    cout << "The sum is " << sum;
}
