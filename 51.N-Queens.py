class Solution:
    def solve(self, col, board, result, rowArray, majorDiagonal, minorDiagonal, n):
        if col == n:
            result.append(board[:])
            return

        for row in range(n):
            if (
                rowArray[row] == 0
                and majorDiagonal[row + col] == 0
                and minorDiagonal[n - 1 + col - row] == 0
            ):
                rowArray[row] = 1
                majorDiagonal[row + col] = 1
                minorDiagonal[n - 1 + col - row] = 1
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                self.solve(
                    col + 1, board, result, rowArray, majorDiagonal, minorDiagonal, n
                )
                rowArray[row] = 0
                majorDiagonal[row + col] = 0
                minorDiagonal[n - 1 + col - row] = 0
                board[row] = board[row][:col] + "." + board[row][col + 1 :]

    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = ["." * n for _ in range(n)]
        rowArray = [0] * n
        majorDiagonal = [0] * (2 * n - 1)
        minorDiagonal = [0] * (2 * n - 1)
        self.solve(0, board, result, rowArray, majorDiagonal, minorDiagonal, n)
        return result
