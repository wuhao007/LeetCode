#include "Expression.h"
#include <stdlib.h>

double Expression::Eval() {
    _busy = true;
    _evaled = true;
    _tokens = SplitDeq(_origExp, ' ');
    _value = _tokens.size() == 0 ? 0 : Reduce();
    _busy = false;
    return _value;
}

double Expression::Reduce() {
    while (_tokens.size() > 0 || _terms.size() != 1) {
        _terms.push_back(Parse(_tokens.front()));
        _tokens.pop_front();
    }
    if (_tokens.size() == 0 && _terms.size() != 1) {
        ostringstream msg;
        msg << "Expression (" << _origExp << ") badly formed - Leftover term detected";
        throw runtime_error(msg.str());
    } else {
        double ret = _terms.front();
        _terms.pop_front();
        return ret;
    }
}

double Expression::Parse(const string& token) {
    if (token.length() == 0) {
        throw runtime_error("Parsing failed: please trim whitespace");
    } else if (IsVal(token)) {
        return atof(token.c_str());
    } else if (IsRef(token)) {
        return Deref(token);
    } else if (IsOp(token)) {
        return Oper(token);
    } else {
        throw runtime_error("Parsing failed with: " + token);
    }
}

double Expression::Deref(const string& s) {
    string::size_type refRow = s[0] - 'A', refCol = atoi(s.substr(1, s.length() - 1).c_str()) - 1;
    if (refRow < 0 || refRow > (_sSheet->size() - 1) || refCol < 0 || refCol > ((*_sSheet)[0].size() - 1)) {
        throw runtime_error("Reference out of bounds");
    } else if ((*_sSheet)[refRow][refCol]._busy) {
        throw runtime_error("Circular Reference detected");
    } else {
        return (*_sSheet)[refRow][refCol].GetValue();
    }
}

double Expression::Oper(const string& token) {
    if (_terms.size() < 2) {
        ostringstream msg;
        msg << "Insufficient terms for Operation at (" << _origExp << ")";
        throw runtime_error(msg.str());
    } else {
        double rVal = _terms.back();
        _terms.pop_back();
        double lVal = _terms.back();
        _terms.pop_back();
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
    if (s.length() < 2) {
        return false;
    } else {
        return ('A' <= s[0] && s[0] <= 'Z') && IsVal(s.substr(1, s.length() - 1));
    }
}

bool Expression::IsOp(const string& s) {
    return s.length() == 1 && (s[0] == '+' || s[0] == '-' || s[0] == '*' || s[0] == '/');
}
