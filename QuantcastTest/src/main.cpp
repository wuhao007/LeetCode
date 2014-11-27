/*
 * Qantcast Spreadsheet Calculator coding challenge
 *
 * by Kevin Cheng, Nov 2012
 *
 * compiled with: g++ (GCC) 4.7.2 20120921 (Red Hat 4.7.2-2)
 */

#include <exception>
#include <vector>
#include <stdio.h>
#include "Utility.h"
#include "Expression.h"

using namespace std;

int main() {
    try {
        // read values
        auto strDim = SplitVec(GetLine(), ' ');
        if (strDim.size() != 2)
            throw runtime_error("Bad dimensions");
        auto cols = atoi(strDim[0].c_str());
        auto rows = atoi(strDim[1].c_str());
        if (rows < 1 || 26 < rows || cols < 1)
            throw runtime_error("Bad dimensions");

        // enter values
        vector<vector<Expression>> sSheet;
        for (auto row = 0; row < rows; ++row) {
            sSheet.push_back(vector<Expression>());
            for (auto col = 0; col < cols; ++col) {
                auto exp = Expression(&sSheet, row, col, GetLine());
                sSheet[row].push_back(exp);
            }
        }

        // evaluate
        cout << cols << " " << rows << endl;
        for (auto &row : sSheet) {
            for (auto &exp : row) {
                printf("%.5f\n", exp.GetValue());
            }
        }

    }
    catch (exception &e) {
        cerr << e.what() << endl;
        return -1;
    }

    return 0;
}

