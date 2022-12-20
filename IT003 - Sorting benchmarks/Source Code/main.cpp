#include"std_sort.h"
#include"quick_sort.h"
#include"heap_sort.h"
#include"merge_sort.h"

const int N = 1e6;
int arr[N];
string stt(int i) {
    if (i == 0) return "QUICK_SORT";
    if (i == 1) return "MERGE_SORT";
    if (i == 2) return "HEAP_SORT";
    return "STD_SORT";
}
vector<double> RUN_TEST(void (*f_sort)(int arr[], int l, int r), string method) {
    vector<double> result;
    bool accepted = true;

    for(int test=1; test<=10; test++) {
        // read input test

        ifstream f;
        f.open("D:\\GitHub\\Sorting\\Data\\output_data\\in" + to_string(test) + ".txt", ios_base:: in);
        for(int i=0; i<N; i++) f >> arr[i];

        // calculate execution time for each input
        clock_t st, en;  double time;
        st = clock();
        f_sort(arr, 0, N - 1);
        en = clock();
        time = (double)(1000*(en - st))/CLOCKS_PER_SEC;
        result.push_back(time);
        f.close();

        if(!is_sorted(arr, arr + N)) accepted = false;
    }

    // check if this sorting method executed successfully
    if(accepted) {
        cout << "\nThuat toan " + method + " chay thanh cong, day da duoc sap xep!\n";
        for(int i=1; i<=10; i++) 
            cout  << "Test " + to_string(i) << ": " << result[i - 1] << '\t';
        cout << endl;
    }
    else cout << "\nThuat toan " + method + " that bai!\n";

    return result;
}

int main() {
    // create data table 4x10 
    vector< vector<double> > data;
    data.resize(4);
    
    data[0] = RUN_TEST(quick_sort, "QUICK_SORT");
    data[1] = RUN_TEST(merge_sort, "MERGE_SORT");
    data[2] = RUN_TEST(heap_sort, "HEAP_SORT");
    data[3] = RUN_TEST(std_sort, "STD_SORT");

    cout << '\n';
    cout << "========== Bang thong ke thoi gian thuc thi cac thuat toan ==========\n";
    cout << setw(12) << "Thuat toan";

    for(int i=1; i<=10; i++) cout << setw(12) << "Test " + to_string(i);
    cout << '\n';
    
    for(int i=0; i<4; i++) {
        cout << setw(12) << stt(i);
        for(int j=0; j<10; j++) cout << setw(12) << data[i][j];
        cout << '\n';
    }
}