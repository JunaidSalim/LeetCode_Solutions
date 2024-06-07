class Solution
{
public:
    bool isValid(string s)
    {
        if (s.size() % 2 != 0)
        {
            return 0;
        }
        stack<char> st;
        for (char c : s)
        {
            if (c == '(' || c == '[' || c == '{')
            {
                st.push(c);
            }
            else
            {
                if (st.empty() || (c == ')' && st.top() != '(') || (c == ']' && st.top() != '[') || (c == '}' && st.top() != '{'))
                {
                    return 0;
                }
                st.pop();
            }
        }
        return st.empty();
    }
};