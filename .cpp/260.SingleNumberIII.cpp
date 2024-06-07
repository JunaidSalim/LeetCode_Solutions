class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        vector<int> result;
        unordered_map <int,int>hashmap;
        for(int num:nums)
        {
            hashmap[num]++;
        }
        for (const auto& pair : hashmap) {
            if (pair.second == 1) {
                result.push_back(pair.first);
            }
        }
        return result;
    }
};