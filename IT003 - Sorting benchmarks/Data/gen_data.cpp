#include<bits/stdc++.h>
#define N int(1e6)
#define MOD int(1e8)
using namespace std;

vector<int> gen() {
    vector<int> vec(N);
    for(int i=0; i<N; i++)
        vec[i] = (rand() * rand()) % MOD;
    return vec;
}

int main() {
    srand(time(NULL));
    for(int i=1; i<=10; i++) {
        ofstream f;
        f.open("D:\\GitHub\\Sorting\\Data\\output_data\\in" + to_string(i) + ".txt");
        vector<int> vec = gen();
        if(i == 1) sort(vec.begin(), vec.end());
        if(i == 2) sort(vec.begin(), vec.end(), greater<int>());
        for(int i=0; i<N; i++)
            f << vec[i] << " ";
        f.close();
        cout << "Test " + to_string(i) << " duoc sinh thanh cong! \n";
    }
}