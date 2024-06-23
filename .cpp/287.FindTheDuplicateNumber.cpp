class Solution {
public:
    int findDuplicate(vector<int>& nums) {
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
        return nums[n-1];
    }
};