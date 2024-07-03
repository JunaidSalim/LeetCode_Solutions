class Solution
{
public:
    double myPow(double x, int n)
    {
        if (n == 0)
        {
            return 1;
        }
        if (x == 1)
        {
            return 1;
        }
        double answer = 1.0;
        long long number = n;
        if (n < 0)
        {
            number = -1 * number;
        }
        while (number > 0)
        {
            if (number % 2)
            {
                answer = answer * x;
                number -= 1;
            }
            else
            {
                x = x * x;
                number = number / 2;
            }
        }
        if (n < 0)
        {
            answer = (double)(1.0) / (double)(answer);
        }
        return answer;
    }
};
