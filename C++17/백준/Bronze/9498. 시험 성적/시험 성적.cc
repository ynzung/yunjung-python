#include <iostream>
using namespace std;

int main()
{
    int score;
    
    cin >> score;
    
    if (score < 0 || score > 100){
        cout << "올바른 점수가 아닙니다." << endl;
    }
    
    else if (90 <= score && score <= 100){
        cout << "A" << endl;
    }
    
    else if (80 <= score && score <= 89){
        cout << "B" << endl;
    }
    
    else if (70 <= score && score <= 79){
        cout << "C" << endl;
    }
    
    else if (60 <= score && score <= 69){
        cout << "D" << endl;
    }
    
    else {
        cout << "F" << endl;
    }
    
    return 0;
}

