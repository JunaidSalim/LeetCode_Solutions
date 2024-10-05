class Solution
{
public:
    void solve(int col, vector<string> &board, vector<vector<string>> &result,
               vector<int> &rowArray, vector<int> &mainDiagonal,
               vector<int> &crossDiagonal, int n)
    {
        if (col == n)
        {
            result.push_back(board);
            return;
        }

        for (int row = 0; row < n; row++)
        {
            if (rowArray[row] == 0 && mainDiagonal[row + col] == 0 && crossDiagonal[n - 1 + col - row] == 0)
            {
                rowArray[row] = 1;
                mainDiagonal[row + col] = 1;
                crossDiagonal[n - 1 + col - row] = 1;
                board[row][col] = 'Q';
                solve(col + 1, board, result, rowArray, mainDiagonal, crossDiagonal, n);
                rowArray[row] = 0;
                mainDiagonal[row + col] = 0;
                crossDiagonal[n - 1 + col - row] = 0;
                board[row][col] = '.';
            }
        }
    }
    vector<vector<string>> solveNQueens(int n)
    {
        vector<vector<string>> result;
        vector<string> board(n);
        string s(n, '.');
        for (int i = 0; i < n; i++)
        {
            board[i] = s;
        }
        vector<int> rowArray(n, 0), mainDiagonal(2 * n - 1, 0),
            crossDiagonal(2 * n - 1, 0);
        solve(0, board, result, rowArray, mainDiagonal, crossDiagonal, n);
        return result;
    }
};