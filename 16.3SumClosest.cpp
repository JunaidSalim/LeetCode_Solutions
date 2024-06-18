class Solution
{
public:
    int threeSumClosest(vector<int> &nums, int target)
    {
        int n = nums.size();
        int min_difference = INT_MAX;
        int result = INT_MAX;
        int left, right, difference, res;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < n; i++)
        {
            left = i + 1;
            right = n - 1;

            while (left < right)
            {
                res = nums[i] + nums[left] + nums[right];
                difference = abs(res - target);

                if (difference < min_difference)
                {
                    min_difference = difference;
                    result = res;
                }

                if (res > target)
                {
                    right--;
                }
                else if (res < target)
                {
                    left++;
                }
                else
                {
                    return res;
                }
            }
        }

        return result;
    }
};