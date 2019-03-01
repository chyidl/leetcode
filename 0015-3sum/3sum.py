# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
#


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # 快速排序 时间复杂度O(nlogn)
        # 2019-03-01 13:30:00 好巧妙 
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                valitional = nums[i] + nums[l] + nums[r]
                if valitional < 0:
                    l += 1
                elif valitional > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
        return result
