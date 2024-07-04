class Solution
{
public:
    vector<int> findDuplicates(vector<int> &nums)
    {
        int n = nums.size();
        int i = 0;
        bool check = false;
        int value = 0;
        while (i < n)
        {
            value = nums[i] - 1;
            check = value >= 0 && value < n;
            if (check && nums[i] != nums[value])
            {
                swap(nums[value], nums[i]);
            }
            else
            {
                i++;
            }
        }
        vector<int> result;
        for (i = 0; i < n; i++)
        {
            if (nums[i] != i + 1)
            {
                result.push_back(nums[i]);
            }
        }
        return result;
    }
};