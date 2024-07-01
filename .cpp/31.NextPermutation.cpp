class Solution
{
public:
    void nextPermutation(std::vector<int> &nums)
    {
        int n = nums.size();
        int index = -1;

        for (int i = n - 1; i > 0; --i)
        {
            if (nums[i] > nums[i - 1])
            {
                index = i - 1;
                break;
            }
        }

        if (index == -1)
        {
            std::reverse(nums.begin(), nums.end());
            return;
        }

        int smallest_index = index + 1;
        for (int i = index + 1; i < n; ++i)
        {
            if (nums[i] > nums[index] && nums[i] <= nums[smallest_index])
            {
                smallest_index = i;
            }
        }

        swap(nums[index], nums[smallest_index]);

        reverse(nums.begin() + index + 1, nums.end());
    }
};