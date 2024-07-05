class Solution
{
public:
    vector<vector<int>> generate(int numRows)
    {
        if (numRows == 0)
        {
            return {};
        }
        vector<vector<int>> result = {{1}};
        for (int i = 0; i < numRows - 1; ++i)
        {
            vector<int> temp;
            temp.push_back(result.back()[0]);
            for (int j = 1; j < result.back().size(); ++j)
            {
                temp.push_back(result.back()[j - 1] + result.back()[j]);
            }
            temp.push_back(result.back().back());
            result.push_back(temp);
        }
        return result;
    }
};