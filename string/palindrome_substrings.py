"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.

Difficulty: Medium
Completed: 7/6/2022
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        return sum(s[i:i+length] == s[i:i+length][::-1] for length in range(1,len(s)+1) for i in range(len(s)+1-length))
        

"""
Explanation:

We return the number of times that a string is the same 
forward and backward for all possible substrings

Time Complexity: O(N^2)
Space Complexity: O(1)
"""
