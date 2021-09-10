# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
#
#  
# Example 1:
#
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
#
#
# Example 2:
#
#
# Input: x = 2.10000, n = 3
# Output: 9.26100
#
#
# Example 3:
#
#
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
#
#
#  
# Constraints:
#
#
# 	-100.0 < x < 100.0
# 	-231 <= n <= 231-1
# 	-104 <= xn <= 104
#
#


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Solution: 递归 + 分治
#         if not n:
#             return 1
#         if n < 0:
#             return 1 / self.myPow(x, -n)
#         # 奇数
#         if n % 2:
#             return x * self.myPow(x, n-1)
#         # 偶数
#         return self.myPow(x*x, n/2)
    
        # Solution: 非递归 
        if n < 0:
            x = 1 / x 
            n = -n 
        pow = 1
        while n:
            if n & 1:
                pow *= x 
            x *= x 
            n >>= 1 
        return pow 
                
