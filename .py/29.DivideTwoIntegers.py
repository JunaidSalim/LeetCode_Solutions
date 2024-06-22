class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend>=0 and divisor<0) or (dividend<0 and divisor>=0) else 1
        divisor = abs(divisor)
        dividend = abs(dividend)
        count=len(range(0,dividend-divisor+1,divisor))
        count = sign * count   
        min_limit = -(2**31)
        max_limit = (2**31) - 1
        count = min(max(min_limit,count),max_limit)
        return count