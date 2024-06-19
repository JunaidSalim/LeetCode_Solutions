class Solution
{
public:
    int firstMissingPositive(vector<int> &nums)
    {
        int n = nums.size();
        int i = 0;

        while (i < n)
        {
            int value = nums[i];
            if (value > 0 && value <= n && nums[value - 1] != value)
            {
                swap(nums[i], nums[value - 1]);
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
                return i + 1;
            }
        }
        return n + 1;
    }
};