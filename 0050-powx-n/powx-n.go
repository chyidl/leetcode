// Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
//
//  
// Example 1:
//
//
// Input: x = 2.00000, n = 10
// Output: 1024.00000
//
//
// Example 2:
//
//
// Input: x = 2.10000, n = 3
// Output: 9.26100
//
//
// Example 3:
//
//
// Input: x = 2.00000, n = -2
// Output: 0.25000
// Explanation: 2-2 = 1/22 = 1/4 = 0.25
//
//
//  
// Constraints:
//
//
// 	-100.0 < x < 100.0
// 	-231 <= n <= 231-1
// 	-104 <= xn <= 104
//
//


func myPow(x float64, n int) float64 {
    // Solution: 递归 + 分治
    // if not n:
    //      return 1
    // if n < 0:
    //  return 1 / myPow(x, -n)
    // 奇数
    // if n % 2:
    //      return x * self.myPow(x, n-1)
    // 偶数
    // return myPow(x*x, n/2)
    var result float64 = 0
    switch {
        case n == 0:
            result = 1
        case n < 0:
            result = 1 / myPow(x, -n)
        case n % 2 == 0:
            result = myPow(x*x, n/2)
        case n % 2 != 0:
            result = x * myPow(x, n-1)
    }
    return result
}
