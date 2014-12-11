#include "Expression.h"
#include <stdlib.h>

double Expression::GetValue(vector<vector<Expression> >& sSheet) {
    if (_color == WHITE) {
        _color = RED;
        deque<string> tokens = SplitDeq(_origExp, ' ');
        _value = tokens.size() == 0 ? 0 : Reduce(sSheet, tokens);
        _color = GREEN;
        _origExp.clear();
        return _value;
    } else if (_color == RED) {
        throw runtime_error("Circular Reference detected");
    } else {
        return _value;
    }
}

double Expression::Reduce(vector<vector<Expression> >& sSheet, deque<string>& tokens) {
    deque<double> terms;
    while (tokens.size() > 0) {
        terms.push_back(Parse(tokens.front(), sSheet, terms));
        tokens.pop_front();
    }

    if (terms.size() != 1) {
        throw runtime_error("Expression (" + _origExp + ") badly formed - Leftover term detected");
    } else {
        double ret = terms.front();
        terms.pop_front();
        return ret;
    }
}

double Expression::Parse(const string& token, vector<vector<Expression> >& sSheet, deque<double>& terms) {
    if (token.length() == 0) {
        throw runtime_error("Parsing failed: please trim whitespace");
    } else if (IsVal(token)) {
        return atof(token.c_str());
    } else if (IsRef(token)) {
        return Deref(token, sSheet);
    } else if (IsOp(token)) {
        return Oper(token, terms);
    } else {
        throw runtime_error("Parsing failed with: " + token);
    }
}

double Expression::Deref(const string& s, vector<vector<Expression> >& sSheet) {
    string::size_type refRow = s[0] - 'A', refCol = atoi(s.substr(1, s.length() - 1).c_str()) - 1;
    if (refRow < 0 || refRow >= sSheet.size() || refCol < 0 || refCol >= sSheet[0].size()) {
        throw runtime_error("Reference out of bounds");
    } else {
        return sSheet[refRow][refCol].GetValue(sSheet);
    }
}

double Expression::Oper(const string& token, deque<double>& terms) {
    if (terms.size() < 2) {
        throw runtime_error("Insufficient terms for Operation at (" + _origExp + ")");
    } else {
        double rVal = terms.back();
        terms.pop_back();
        double lVal = terms.back();
        terms.pop_back();
        switch (token[0]) {
            case '+': 
                return lVal + rVal;
            case '-': 
                return lVal - rVal;
            case '*': 
                return lVal * rVal;
            case '/':
                return lVal / rVal;
            default: 
                throw runtime_error("Unrecognized operation");
        }
    }
}

bool Expression::IsVal(const string& s) {
    return  (s[0] == '-' || ('0' <= s[0] && s[0] <= '9')) && ('0' <= s[s.length() - 1] && s[s.length() - 1] <= '9');
}

bool Expression::IsRef(const string& s) {
    return s.length() >= 2 && ('A' <= s[0] && s[0] <= 'Z') && IsVal(s.substr(1, s.length() - 1));
}

bool Expression::IsOp(const string& s) {
    return s.length() == 1 && (s[0] == '+' || s[0] == '-' || s[0] == '*' || s[0] == '/');
}
