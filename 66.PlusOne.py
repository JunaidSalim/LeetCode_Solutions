class Solution(object):
    def plusOne(self, digits):
        result = list(reversed(digits))
        result[0] += 1
        if result[0]<10:
            return list(reversed(result))
        else:
            length = len(result)
            for i in range(length):
                if result[i]==10:
                    result[i]=0
                    if i==length-1:
                        result.append(1)
                    else:
                        result[i+1]+=1
            return list(reversed(result))
