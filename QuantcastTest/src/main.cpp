#include <exception>
#include <vector>
#include <stdio.h>
#include "Utility.h"
#include "Expression.h"
#include <stdlib.h>
using namespace std;
int main() {
    try {
        // read values
        vector<string> strDim = SplitVec(GetLine(), ' ');
        if (strDim.size() != 2) {
            throw runtime_error("Bad dimensions");
        }
        int cols = atoi(strDim[0].c_str());
        int rows = atoi(strDim[1].c_str());
        if (rows < 1 || rows > 26 || cols < 1) {
            throw runtime_error("Bad dimensions");
        }
        // enter values
        vector<vector<Expression> > sSheet;
        for (int row = 0; row < rows; ++row) {
            sSheet.push_back(vector<Expression>());
            for (int col = 0; col < cols; ++col) {
                sSheet[row].push_back(Expression(&sSheet, GetLine()));
            }
        }
        // evaluate
        cout << cols << " " << rows << endl;
        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                printf("%.5f\n", sSheet[row][col].GetValue());
            }
        }
        return 0;
    } catch (exception& e) {
        cerr << e.what() << endl;
        return -1;
    }
}
