#include <iostream>
using namespace std;

int main()
{
    int testCase, a, b;
    cin >> testCase;
    
    for (int i = 1; i <= testCase; i++) {
        cin >> a >> b;
        cout << a + b << endl;
    }
    return 0;
}
