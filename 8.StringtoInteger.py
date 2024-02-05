class Solution(object):
    def myAtoi(self, s):
        if not s:
            return 0

        n = len(s)
        signs = "+-"
        sign, result, check_alpha, check_for_sign, check_space = 1, "", False, False, False

        for i in range(n):
            if s[i].isalpha():
                return 0 if not check_alpha else min(max(int(result) * sign, -2147483648), 2147483647)
            elif s[i].isdigit():
                check_alpha, check_for_sign, check_space = True, True, True
                result += s[i]
            elif s[i] in signs:
                if check_alpha and result:
                    return min(max(int(result) * sign, -2147483648), 2147483647)
                if check_for_sign or check_space:
                    return 0
                sign = -1 if s[i] == "-" else 1
                check_for_sign = True
            elif s[i] == " ":
                if check_alpha or check_for_sign or result:
                    break
            elif s[i] == ".":
                return min(max(int(result) * sign, -2147483648), 2147483647) if result else 0
            else:
                break
        return min(max(int(result) * sign, -2147483648), 2147483647) if result else 0
