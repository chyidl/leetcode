# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#
#  
#


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        # 2019-02-28 23:53:00 The First Edition 
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        """ 
        for i in range(len(nums)):
            diff = target - nums[i]
            try:
                other = nums.index(diff)
                if other != i:
                    return [i, other]
            except:
                pass 
