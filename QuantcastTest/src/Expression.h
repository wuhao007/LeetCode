#ifndef EXPRESSION_H
#define EXPRESSION_H
#include <deque>
#include <iostream>
#include <stdexcept>
#include <string>
#include <sstream>
#include <vector>
#include "Utility.h"
using namespace std;
class Expression {
    public:
        Expression(const string& exp): 
            _origExp(exp), _color(WHITE) {}
        double GetValue(vector<vector<Expression> >& sSheet);
    private:
        typedef enum color {RED, WHITE, GREEN} color;
        string _origExp;
        double _value;
        color _color;

        double Reduce(vector<vector<Expression> >& sSheet, deque<string>& tokens);
        double Parse(const string& token, vector<vector<Expression> >& sSheet, deque<double>& terms);
        double Oper(const string& token, deque<double>& terms);
        double Deref(const string& s, vector<vector<Expression> >& sSheet);

        bool IsVal(const string& s);
        bool IsRef(const string& s);
        bool IsOp(const string& s);
};
#endif
