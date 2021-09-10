# Given a non-negative integer x, compute and return the square root of x.
#
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
#
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
#
#  
# Example 1:
#
#
# Input: x = 4
# Output: 2
#
#
# Example 2:
#
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
#
#  
# Constraints:
#
#
# 	0 <= x <= 231 - 1
#
#


class Solution:
    def mySqrt(self, x: int) -> int:
        # 逼近二分法 -- 单调递增 
        # if (x==0 or x==1): return x
        # l=1; r=x; res=0
        # while l <= r:
        #     mid = (l+ r)//2
        #     if mid == x//mid:
        #         return mid 
        #     elif mid > x//mid:
        #         r = mid - 1
        #     else:
        #         l = mid + 1 
        #         res = mid 
        # return res 
    
        # solution: 牛顿迭代法 
        r = x 
        while r * r > x:
            r = (r + x // r) // 2
        return r 
        
