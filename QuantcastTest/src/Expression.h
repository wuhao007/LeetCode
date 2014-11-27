#pragma once
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
        Expression(vector<vector<Expression>> *sSheet,
                   int row, int col, const string &exp);

        string GetExp() { return _origExp; }

        double GetValue() { return _evaled ? _value : Eval(); }

    private:
        vector<vector<Expression>> *_sSheet;

        int _row;
        int _col;
        string _origExp;
        double _value;
        
        bool _evaled;
        bool _busy;

        deque<string> _tokens;
        deque<double> _terms;

        double Eval();
        double Reduce();
        double Parse(const string &token);
        double Oper(const string &token);
        double Deref(const string &s);

        bool IsVal(const string &s);
        bool IsRef(const string &s);
        bool IsOp(const string &s);
};

#endif
