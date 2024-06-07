class Solution {
public:
    bool isPalindrome(int x) {
       long  int rev=0;
    int orig=x;
    while(x!=0)
    {
        rev = (rev*10) + (x%10);
        x=x/10;
    }
    if(rev==orig && rev>=0){
        return true;
    }
    else
    {
        return false;
    }

    }
};
