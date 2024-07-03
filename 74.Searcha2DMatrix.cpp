class Solution
{
public:
    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        int rows = matrix.size();
        int columns = matrix[0].size();
        int top = 0, bottom = rows - 1;

        while (top <= bottom)
        {
            int row = (top + bottom) / 2;
            if (matrix[row][0] > target)
            {
                bottom = row - 1;
            }
            else if (matrix[row][columns - 1] < target)
            {
                top = row + 1;
            }
            else
            {
                break;
            }
        }

        if (top > bottom)
        {
            return false;
        }

        int row = (top + bottom) / 2;
        int left = 0, right = columns - 1;
        while (left <= right)
        {
            int mid = (left + right) / 2;
            if (matrix[row][mid] > target)
            {
                right = mid - 1;
            }
            else if (matrix[row][mid] < target)
            {
                left = mid + 1;
            }
            else
            {
                return true;
            }
        }

        return false;
    }
};
