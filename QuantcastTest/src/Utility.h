#ifndef UTILITY_H
#define UTILITY_H
#include <deque>
#include <iostream>
#include <sstream>
using namespace std;
deque<string> SplitDeq(const string& str, const char& delim);
string GetLine();
#endif
