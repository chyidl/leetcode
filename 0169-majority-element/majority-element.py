# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
#


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        # 2019-03-01 13:45  时间复杂度O(n*nlog(n)) 
        # Runtime: 48ms 
        threshold = len(nums)//2
        res = dict() 
        unions = set(nums)
        for num in unions:
            count = nums.count(num)
            if count > threshold:
                res[count] = num 
        return res[max(res.keys())]
        
        # Time complexity: O(n) 
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
        """
        nums.sort()
        return nums[len(nums)//2]
