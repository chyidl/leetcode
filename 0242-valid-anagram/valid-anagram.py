# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
#  
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#  
# Constraints:
#
#
# 	1 <= s.length, t.length <= 5 * 104
# 	s and t consist of lowercase English letters.
#
#
#  
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
#


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False 
        
        # solution 1: 排序 比较 
        # nLog(n)
        # return sorted(s) == sorted(t)
    
        # solution 2: Map Count {letter: Count}
        dic1, dic2 = {}, {} 
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1 
        return dic1 == dic2
        
