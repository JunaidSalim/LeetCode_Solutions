class Solution {
public:
    int strStr(string haystack, string needle) {
        int count=0;
        for(int i=0;i<haystack.length();i++)
        {
            if(needle[0]==haystack[i])
            {
                for(int j=0;j<needle.length();j++)
                {
                    if(needle[j]==haystack[i+j])
                    {
                        count++;
                        if(count == needle.length())
                        {
                            return i;
                        }
                    }
                    else{
                        count =0;
                        break;
                    }
                }
            }
        }
        return -1;

    }
};
