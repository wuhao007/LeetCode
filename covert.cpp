#include<iostream>
#include<string>
#include<vector>

using namespace std;

char * smallconver(int input) {
}

char * covert(int input) {
    int tmp = 0;
    int cnt = 0;
    string res = "";
    vector<string> v;
    v.push_back("");
    v.push_back("thoursands");
    v.push_back("million");
    v.push_back("billion");
    int b = 0;
    while (input > 0) {
        res = smallconver(input % 1000) + " " + v[b] + " " + res;
        b++;
        input /= 1000;
    }
    return res.c_str();
}
