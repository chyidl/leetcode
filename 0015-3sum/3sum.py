# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#  
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
#
#  
# Constraints:
#
#
# 	0 <= nums.length <= 3000
# 	-105 <= nums[i] <= 105
#
#


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Solution: 暴力求解 O(n^3)
        
        # Solution: Set O(n^2)
        
        # Solution: SortFind O(nlogn) O(n^2) 
        if len(nums) < 3: return []
        nums.sort() 
        res = set()
        for i, v in enumerate(nums[:-2]):
            # 跳过重复
            if i >= 1 and v == nums[i-1]:
                continue
            d = {} 
            for x in nums[i+1:]:
                if x not in d:
                    # flag
                    d[-(v+x)] = True
                else:
                    res.add((v, -v-x, x))
        return map(list, res)
