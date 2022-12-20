#include<bits/stdc++.h>
using namespace std;

string LOW = "abcdefghijklmnopqrstuvwxyz", UP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

char shift(char c, int k) {
   if(islower(c)) return LOW[(LOW.find(c) + k) % 26];
   if(isupper(c)) return UP[(UP.find(c) + k)%26];
   return c;
}

string decrypt(string plain, int key) {
   string cipher = "";
   for(char c: plain) cipher += shift(c, key);
   return cipher;
}

int main() {
   cout << "Caesar decryption - bruteforce key\n";
   string ciphertext;
   cout << "Enter your ciphertext: "; getline(cin, ciphertext);
   for(int key=1; key<26; key++) {
       string flag = decrypt(ciphertext, key);
       cout << "Plaintext with key = " << key << " : " << flag << '\n';
   }

    // VD: lay tu crypto challenge angstromctf 2022:
    // ciphertext: sulx{klgh_jayzl_lzwjw_ujqhlgyjshzwj_kume}
    // Thu bruteforce thi thay key = 8 ta tim duoc flag la: actf{stop_right_there_cryptographer_scum}
}