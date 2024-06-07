class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int length = strs[0].size();
        bool check;
        string str="";
        char c;
        for(int i =0;i<length;i++)
        {
            int len = strs.size();
            c = strs[0][i]; 
            check=true;
            for(int j=1;j<len;j++)
            {
                if(c!=strs[j][i])
                {
                    check = false;
                    break;
                }
            }
            if(check)
            {
                str+=strs[0][i];
            }
            else{
                break;
            }
        }
        return str;
    }
};