# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
#
# Input: [1,2,0]
# Output: 3
#
#
# Example 2:
#
#
# Input: [3,4,-1,1]
# Output: 2
#
#
# Example 3:
#
#
# Input: [7,8,9,11,12]
# Output: 1
#
#
# Note:
#
# Your algorithm should run in O(n) time and uses constant extra space.
#


class Solution:
    def firstMissingPositive(self, nums) -> int:
        if not nums:
            return 1
        counter = collections.Counter(nums)
        maxNum = max(counter.keys())
        i = 1
        while i < maxNum:
            if counter[i] == 0:
                return i
            else:
                i += 1
        return (maxNum if maxNum > 0 else 0)+ 1
