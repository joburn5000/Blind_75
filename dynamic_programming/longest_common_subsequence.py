"""
Given two strings text1 and text2, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some 
characters (can be none) deleted without changing the relative order of the remaining 
characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

Difficulty: Medium
Completed: 6/9
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dynamic programming array
        dp = [[0 for i in range(len(text2))] for j in range(len(text1))]
        
        # set up first row and first column of the dp array
        if text1[0] == text2[0]: dp[0][0] = 1
        for i in range(1, len(text1)):
            dp[i][0] = 1 if text1[i]==text2[0] or dp[i-1][0] else 0
        for j in range(1, len(text2)):
            dp[0][j] = 1 if text1[0]==text2[j] or dp[0][j-1] else 0 
        
        # fill in the rest of the dp array
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]: dp[i][j] = dp[i-1][j-1]+1  # letters are the same
                else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])        # letters are different
        
        return max(map(max,dp))
"""
Explanation:

We use dynamic programming to store the values in array dp where dp[i][j] is the largest
common subsequence for text1 from index 0 to i and text2 from 0 to j

Time Complexity: O(N*M)
"""
