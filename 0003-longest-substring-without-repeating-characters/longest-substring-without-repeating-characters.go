// Given a string s, find the length of the longest substring without repeating characters.
//
//  
// Example 1:
//
//
// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
//
//
// Example 2:
//
//
// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
//
//
// Example 3:
//
//
// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
//
//
//  
// Constraints:
//
//
// 	0 <= s.length <= 5 * 104
// 	s consists of English letters, digits, symbols and spaces.
//
//


func lengthOfLongestSubstring(s string) int {
    // rune like int32 
    // left 左边位置坐标
    m, max, left := make(map[rune]int), 0, 0
    // pwwkew
    for idx, c := range s {
        if _, okay := m[c]; okay && m[c] >= left {
            if idx-left > max {
                max = idx - left
            }
            left = m[c] + 1
        }
        m[c] = idx
    }
    if len(s) - left > max {
        max = len(s) - left
    }
    return max
}
