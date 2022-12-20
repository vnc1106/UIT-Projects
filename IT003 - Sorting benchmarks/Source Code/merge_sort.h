#include<bits/stdc++.h>
using namespace std;

void merge(int arr[], int l, int m, int r) {
    vector<int> a(arr + l, arr + m + 1);
    vector<int> b(arr + m + 1, arr + r + 1);
    int i = 0, j = 0;
    while(i < a.size() && j < b.size()) {
        if(a[i] <= b[j]) {
            arr[l] = a[i]; ++l; ++i;
        }       
        else {
            arr[l] = b[j]; ++l; ++j;
        }
    }   
    while(i < a.size()) {
        arr[l] = a[i]; ++l; ++i;
    }
    while(j < b.size()) {
        arr[l] = b[j]; ++l; ++j;
    }
}
void merge_sort(int arr[], int l, int r) {
    if(l == r) return;
    int m = (l + r)/2;
    merge_sort(arr, l, m);
    merge_sort(arr, m + 1, r);
    merge(arr, l, m, r);
}