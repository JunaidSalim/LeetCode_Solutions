c
lass Solution {
public:
    int reverse(int x) {
        long int num=0;
        while(x!=0)
        {
            if((num*10)< (pow(2,31)-1) && (num*10)> -(pow(2,31))){
            num =(num *10) +( x %10);
            x/=10;}
            else{
                return 0;
            }
        }
        return num;
    }
};
