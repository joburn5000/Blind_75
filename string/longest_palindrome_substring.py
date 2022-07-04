"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

Difficulty: Medium
Completed: 1/19/2022
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # check longest first:
        i, j = 0, len(s)
        while i < len(s)-1:
            string = s[i:i+j]
            if (string == string[::-1]):
                return string
            
            i+=1
            if (i+j > len(s)):
                j -= 1
                i = 0
        return s[0]
    
        
        """
        # brute force:
        
        longest_palindrome = s[0]
        
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                string = s[i:j+1]
                is_palindrome = string == string[::-1]
                if is_palindrome  & (len(string) > len(longest_palindrome)):
                    longest_palindrome = string
                    
        return longest_palindrome
        """

"""
Explanation:

We start by checking the longest possible substrings (the length of s)
and work our way down to the shortest possible substring. When we find any
match, we return that value.

Time Complexity: O(N^2)
Space Complexity: O(1)
"""
