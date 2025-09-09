#include <iostream>
#include <queue>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N, K;
    cin >> N >> K;
    queue <int> qe;
    
    for (int i = 1; i <= N; i++){
        qe.push(i);
    }
    cout << '<';
    
    while (!qe.empty()) {
        for(int i = 1; i <= K; i++) {
            int tmp = qe.front();
            qe.pop();
            
            if(i != K) {
                qe.push(tmp);
            }
            else {
                cout << tmp;
                if(!qe.empty()) cout << ", ";
            }
        }
    }
    cout << '>' << '\n';
    
}
