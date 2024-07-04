class Solution
{
public:
    vector<int> findDisappearedNumbers(vector<int> &nums)
    {
        int n = nums.size();
        int i = 0;
        vector<int> result;
        while (i < n)
        {
            int value = nums[i] - 1;
            if (value >= 0 && value < n && nums[value] != nums[i])
            {
                swap(nums[i], nums[value]);
            }
            else
            {
                i++;
            }
        }
        for (i = 0; i < n; i++)
        {
            if (nums[i] != i + 1)
            {
                result.push_back(i + 1);
            }
        }
        return result;
    }
};