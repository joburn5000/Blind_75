"""
You are given a string s and an integer k. You can choose any character 
of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter 
you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

Difficulty: Medium
Completed: 7/9/2022
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int: # output = 10, k = 5, used 4 we need at least 5
        counts = {}
        l,r = 0,0
        most_frequent = s[0]
        while r < len(s):
            letter = s[r]
            # increment this letter's count
            counts[letter] = counts.get(letter,0) + 1
            # update most frequent letter if necessary
            if counts[letter] > counts[most_frequent]:
                most_frequent = letter
            # shift left pointer if the # of letters that need to be replaced > k 
            if r+1-l-counts[most_frequent] > k:
                counts[s[l]] -= 1
                l+=1
            r+=1
        return r-l
        
        

"""
Explanation:

We use shifting windows with a right pointer (r) and left pointer (l)
to check for the longest substring where there are at most k letters
that need to be replaced.

We keep shifting the right pointer one every iteration. If we ever find
that we have too many letters that need to be replaced, we simply shift
the left pointer to the right.

Time Complexity: O(N)
Space Complexity: O(1)
"""
