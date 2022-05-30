#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;
//xor function
string XOR(string a, string b) {
    string result = "";
    for (int i = 0; i < a.length(); i++) {
        char current = a[i];
        char currentKey = b[i % b.length()];
        result += current ^ currentKey;
    }
    return result;
}
//main
int main() {
    auto start = high_resolution_clock::now();
    string a = "Hello World!";
    string b = "x";
    string result = XOR(a, b);
    //print result as hex
    cout << "{ ";
    for (int i = 0; i < result.length(); i++) {
        if (i == result.length() - 1) {
            cout << hex << "0x" << (int) result[i] << " };" << endl;
            return 0;
        }
        cout << hex << "0x" <<(int)result[i] << ", ";
    }
    return 0;
}