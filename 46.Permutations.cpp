class Solution
{
public:
    int factorial(int n)
    {
        int result = 1;
        for (int i = 2; i <= n; ++i)
        {
            result *= i;
        }
        return result;
    }
    vector<int> nextPermutation(vector<int> &nums)
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
            reverse(nums.begin(), nums.end());
            return nums;
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
        return nums;
    }

    vector<vector<int>> permute(vector<int> &nums)
    {
        vector<vector<int>> result;
        vector<int> prev = nums;
        result.push_back(prev);
        int n = factorial(nums.size());
        for (int i = 0; i < n - 1; ++i)
        {
            vector<int> next_perm = nextPermutation(prev);
            result.push_back(next_perm);
            prev = next_perm;
        }
        return result;
    }
};