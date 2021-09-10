# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#
#  
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#  
# Constraints:
#
#
# 	n == nums.length
# 	1 <= n <= 5 * 104
# 	-231 <= nums[i] <= 231 - 1
#
#
#  
# Follow-up: Could you solve the problem in linear time and in O(1) space?


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution: Map count 
        map = {} 
        for num in nums:
            map[num] = map.get(num, 0) + 1 
        for key, val in map.items():
            if val >= len(nums)/2:
                return key 
            
        # Solution: Sort -> 
        # Solution: Divide & Conquer 
