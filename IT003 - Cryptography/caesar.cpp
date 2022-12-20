#include<bits/stdc++.h>
using namespace std;

string LOW = "abcdefghijklmnopqrstuvwxyz", UP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

char shift(char c, int k) {
   if(islower(c)) return LOW[(LOW.find(c) + k) % 26];
   if(isupper(c)) return UP[(UP.find(c) + k)%26];
   return c;
}

string encrypt(string plain, int key) {
   string cipher = "";
   for(char c: plain) cipher += shift(c, key);
   return cipher;
}

int main() {
   cout << "Caesar encryption\n";
   string plaintext;
   cout << "Enter your plaintext: "; getline(cin, plaintext);
   int key;
   cout << "Enter your shift key: "; cin >> key;
   cout << "Your encrypted plaintext: " << decrypt(plaintext, key);

}