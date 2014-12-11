#include <exception>
#include <stdio.h>
#include "Utility.h"
#include "Expression.h"
#include <stdlib.h>
using namespace std;
int main() {
    try {
        deque<string> strDim = SplitDeq(GetLine(), ' ');
        if (strDim.size() != 2) {
            throw runtime_error("Bad dimensions");
        }
        int cols = atoi(strDim.front().c_str());
        strDim.pop_front();
        int rows = atoi(strDim.front().c_str());
        strDim.pop_front();
        if (rows < 1 || rows > 26 || cols < 1) {
            throw runtime_error("Bad dimensions");
        }
        vector<vector<Expression> > sSheet;
        for (int row = 0; row < rows; ++row) {
            sSheet.push_back(vector<Expression>());
            for (int col = 0; col < cols; ++col) {
                sSheet[row].push_back(Expression(GetLine()));
            }
        }
        cout << cols << " " << rows << endl;
        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                printf("%.5f\n", sSheet[row][col].GetValue(sSheet));
            }
        }
        return 0;
    } catch (exception& e) {
        cerr << e.what() << endl;
        return -1;
    }
}
