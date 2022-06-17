"""

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.


Difficulty: Medium
Completed: 5/17/2022

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        
        length = 1
        substring = s[0]
        
        for i in range(1,len(s)):
            if s[i] in substring:                               # current letter is in substring
                if len(substring) > length:                     # check if substring is longest so far
                    length = len(substring)                     # if so, update the length
                substring = substring[substring.index(s[i])+1:] # shorten the substring to not include that letter
                
            substring += s[i]                                   # add the letter to substring
            
        if len(substring) > length:                             # check final substring
            length = len(substring)
            
        return length
"""
Explanation:

The pig picture algorithm is to make substrings as large as possible.
When a letter is already in the substring, we shorten that substring
to remove everything including and before that repeated letter,
because there is no unchecked substring that could be larger using
that letter.

Time Complexity: O(N)
Space Complexity: O(N)
"""
