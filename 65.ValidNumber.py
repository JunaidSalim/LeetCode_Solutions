class Solution(object):
    def isNumber(self, s):
        if s.count("e")>1 or s.count("E")>1 or s.count(".")>1:
            return False
        n = len(s)
        numbers = "0123456789"
        signs ="+-"
        temp =""
        for i in range(n):
            if s[i] in "eE":
                if i==0 or i==n-1:
                    return False
                elif (s[i+1] in numbers or s[i+1] in signs) and s[i-1] in numbers:
                    temp+=s[i]
                    continue
                else:
                    if s[i-1] in ".":
                        if i-1==0:
                            return False
                        else:
                            if s[i-2] in numbers:
                                temp+=s[i]
                                continue
                            else:
                                return False
                    return False
            elif s[i] in signs:
                if i==n-1:
                    return False
                elif i!=0:
                    if s[i-1] in "eE":
                        temp+=s[i]
                        continue
                    else:
                        return False
                elif s[i] in temp:
                    return False
                elif s[i+1] in numbers or s[i+1] in ".":
                    temp+=s[i]
                    continue
                else:
                    return False
            elif s[i] in ".":
                if s[i] in temp:
                    return False
                elif i==n-1:
                    if s[i-1] not in numbers:
                        return False
                    else:
                        if "e" in temp:
                            return False
                        temp+=s[i]
                        continue
                else:
                    if "e" in temp:
                        return False
                    temp+=s[i]
                    continue
            elif s[i] in numbers:
                continue
            else:
                return False
        return True