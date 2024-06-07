class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int>left_product (n,1);
        vector<int>right_product (n,1);
        for (int i =1;i<n;i++)
        {
            left_product[i] = left_product[i-1] * nums[i-1];
        }
        for (int i =n-2;i>-1;i--)
        {
            right_product[i] = right_product[i+1] * nums[i+1];
        }
        vector<int> result(n,1);
        for (int i =0;i<n;i++)
        {
            result[i] = left_product[i] * right_product[i];
        }
        return result;
    }
};