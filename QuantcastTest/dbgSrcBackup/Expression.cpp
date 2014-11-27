#include "Expression.h"

Expression::Expression(vector<vector<Expression>> *sSheet,
                       int row, int col, const string &exp) :
    _sSheet(sSheet), _row(row), _col(col), _origExp(exp),
    _evaled(false), _busy(false) { }

// lex full expression into tokens and evaluate
double Expression::Eval() {
#if DEBUG
    cout << "Eval  (" << _row << "," << _col << ") " \
         << this << " = " << _value << " " << _evaled << endl;
#endif
    _busy = true;
    _evaled = true;
    _tokens = SplitDeq(_origExp, ' ');
#if DEBUG
    cout << "_origExp: " << _origExp << endl;
    cout << "_tokens.size(): " << _tokens.size() << endl;
    cout << "_tokens[0]: " << _tokens[0] << endl;
#endif

    _value = _tokens.size() == 0 ? 0 : Reduce();

    _busy = false;
    return _value;
}

// parse a token into a term each iteration
double Expression::Reduce() {
    while (_tokens.size() > 0 || _terms.size() != 1) {
#if DEBUG
        cout << "Reducing " << _tokens.size();
        cout << ":" << _terms.size() << endl;
#endif
        if (_tokens.size() == 0 && _terms.size() != 1) {
            ostringstream msg;
            msg << "Expression (" << _row << "," << _col << \
                ") badly formed - Leftover term detected";
            throw runtime_error(msg.str());
        }
        _terms.push_back(Parse(_tokens.front()));
        _tokens.pop_front();
    }
    auto ret = _terms.front();
    _terms.pop_front(); // should be the last term
    return ret;
}

// parse 1-token expression
double Expression::Parse(const string &token) {
#if DEBUG
    cout << "Parsing :" << token << endl;
#endif
    if (token.length() < 1)
        throw runtime_error("Parsing failed: please trim whitespace");
    if (IsVal(token)) {
#if DEBUG
        cout << " IsVal" << endl;
#endif
        return atof(token.c_str());
    }
    if (IsRef(token)) {
#if DEBUG
        cout << " IsRef" << endl;
#endif
        return Deref(token);
#if DEBUG
        cout << " DoneRef" << endl;
#endif
    }
    if (IsOp(token)) {
#if DEBUG
        cout << " IsOp : ";
#endif
        return Oper(token);
    }
    throw runtime_error("Parsing failed with: " + token);
}

// dereference a spreadsheet reference
double Expression::Deref(const string &s) {
    auto refRow = s[0] - 'A';
    auto refCol = atoi(s.substr(1, s.length() - 1).c_str()) - 1;
    int rows = _sSheet->size();
    int cols = (*_sSheet)[0].size();
#if DEBUG  
    ostringstream out;
    out << "Deref (" << refRow << "," << refCol << ") " \
        << &((*_sSheet)[refRow][refCol]);
    cout << out.str() << endl;
#endif 
    if (refRow < 0 || rows - 1 < refRow ||
        refCol < 0 || cols - 1 < refCol)
        throw runtime_error("Reference out of bounds");
    if ((*_sSheet)[refRow][refCol]._busy)
        throw runtime_error("Circular Reference detected");
    return (*_sSheet)[refRow][refCol].GetValue();
}

// apply an arithmetic operation
double Expression::Oper(const string &token) {
    if (_terms.size() < 2) {
        ostringstream msg;
        msg << "Parsing failed: insufficient terms for Op at (" << \
            _row << "," << _col << ")";
        throw runtime_error(msg.str());
    }
    auto rVal = _terms.back();
    _terms.pop_back();
    auto lVal = _terms.back();
    _terms.pop_back();

    switch (token[0]) {
        case '+': return lVal + rVal;
        case '-': return lVal - rVal;
        case '*': return lVal * rVal;
        case '/': return lVal / rVal;
        default: return 0;
    }
#if DEBUG
    cout << lVal << token << rVal << "=" << _terms.back() << endl;
#endif
}

bool Expression::IsVal(const string &s) {
    return  (s[0] == '-' || ('0' <= s[0] && s[0] <= '9')) &&
            ('0' <= s[s.length() - 1] && s[s.length() - 1] <= '9');
}

bool Expression::IsRef(const string &s) {
    if (s.length() < 2) return false;
    auto ltr = s[0];
    auto num = s.substr(1, s.length() - 1);
    return ('A' <= ltr && ltr <= 'Z') && IsVal(num);
}

bool Expression::IsOp(const string &s) {
    return s.length() == 1 &&
           (s[0] == '+' || s[0] == '-' ||
            s[0] == '*' || s[0] == '/');
}

