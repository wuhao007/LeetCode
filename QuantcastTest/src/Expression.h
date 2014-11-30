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
        Expression(vector<vector<Expression> >* sSheet, const string& exp):
                _sSheet(sSheet), _origExp(exp), _evaled(false), _busy(false) {}
        double GetValue() { return _evaled ? _value : Eval(); }
    private:
        vector<vector<Expression> >* _sSheet;

        string _origExp;
        double _value;
        
        bool _evaled;
        bool _busy;

        deque<string> _tokens;
        deque<double> _terms;

        double Eval();
        double Reduce();
        double Parse(const string& token);
        double Oper(const string& token);
        double Deref(const string& s);

        bool IsVal(const string& s);
        bool IsRef(const string& s);
        bool IsOp(const string& s);
};
#endif
