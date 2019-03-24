# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# 	Open brackets must be closed by the same type of brackets.
# 	Open brackets must be closed in the correct order.
#
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: "{[]}"
# Output: true
#
#


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        rule_dict = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if i in rule_dict.keys() and rule_dict[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)
        if not stack:
            return True
        else:
            return False
            
