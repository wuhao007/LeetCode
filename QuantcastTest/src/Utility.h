#pragma once
#ifndef UTILITY_H
#define UTILITY_H

#include <deque>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

vector<string> SplitVec(const string &str, const char &delim);
deque<string> SplitDeq(const string &str, const char &delim);
string GetLine();

#endif
