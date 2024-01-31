class Solution(object):
    def addBinary(self, a, b):
        result = []
        carry = 0
        big = list(a) if len(a) >= len(b) else list(b)
        small = list(a) if len(a) < len(b) else list(b)
        length = min(len(a), len(b))
        diff = len(big) - len(small)
        for i in range(length - 1, -1, -1):
            if big[i + diff] == '1' and small[i] == '1':
                result.append(0 if carry == 0 else 1)
                carry = 1
            else:
                current_sum = carry + int(small[i]) + int(big[i + diff])
                if current_sum > 1:
                    result.append(0)
                    carry = 1
                else:
                    result.append(current_sum)
                    carry = 0
        for i in range(max(len(a), len(b)) - length - 1, -1, -1):
            current_sum = carry + int(big[i])
            if current_sum > 1:
                result.append(0)
                carry=1
            else:
                result.append(current_sum)
                carry = 0
        if carry == 1:
            result.append(1)
        res = ''.join(map(str, result[::-1]))
        return res

