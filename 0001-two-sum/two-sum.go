// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
//
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
//
// You can return the answer in any order.
//
//  
// Example 1:
//
//
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
//
//
// Example 2:
//
//
// Input: nums = [3,2,4], target = 6
// Output: [1,2]
//
//
// Example 3:
//
//
// Input: nums = [3,3], target = 6
// Output: [0,1]
//
//
//  
// Constraints:
//
//
// 	2 <= nums.length <= 104
// 	-109 <= nums[i] <= 109
// 	-109 <= target <= 109
// 	Only one valid answer exists.
//
//
//  
// Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


func twoSum(nums []int, target int) []int {
    /*
        解题思路:
            1. 首先使用map存储数字和下标的映射关系: 
            2. 查找map中是否符合 target - thisNum的存储是指
    
        时间复杂度: 最坏情况 O(n) 需要一次完整遍历
        空间复杂度: O(n)
    */
    
    // map fast lookups, adds, and delete
    seenNums := make(map[int]int)
    for index, thisNum := range nums {
        if seenIndex, ok := seenNums[target - thisNum]; ok {
            return []int{seenIndex, index}
        }
        seenNums[thisNum] = index
    }
    return []int{0,0} // Should not happen
}
