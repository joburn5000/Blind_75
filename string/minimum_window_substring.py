"""
Given two strings s and t of lengths m and n respectively, return 
the minimum window substring of s such that every character in t 
(including duplicates) is included in the window. If there is no 
such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 
Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', 
and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?

Difficulty: Hard
Completed: 7/8/2022
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = ""
        dictionary = Counter(t)
        required, formed = len(dictionary), 0
        l,r = 0,0
        counts = {}
        while r < len(s):
            letter = s[r]
            # increment the count for that letter
            counts[letter] = counts.get(letter, 0) + 1
            
            # check if we have reached our target for that letter
            if letter in dictionary and counts[letter] == dictionary[letter]:
                formed += 1
            
            # shorten the window as much as possible
            while l <= r and formed == required:
                letter = s[l]
                
                # update output if the substring is smaller
                if not output or r-l < len(output):
                    output = s[l:r+1]
                counts[letter] -= 1
                # check if we have taken off too many letters (no longer a valid substring)
                if letter in dictionary and counts[letter] < dictionary[letter]:
                    formed -= 1
                # shift the left pointer
                l+=1
            # shift the right pointer
            r+=1
        return output
        

"""
Explanation:

We use sliding windows to search for a valid substring. We keep track of the
windows using l and r, the left and right pointers.

The dictionary counts contains the count for every character in our current
window substring. The variable formed keeps track of how many letters we have
in the substring that match with letters in t. The variable required tells us
how many letters we have to match in order for the substring to be valid. When
formed == required, the substring has all the letters in t at least once.

We start by increasing r until we find a substring that contains all the letters
in t. Then we shrink the window by increasing l until we find that the window
no longer contains all the letters we need. We then increase r until the window does,
then increase l until it doesn't, and so on until the end. We keep track of the
smallest length substring and store it in output.

Time Complexity: O(M + N) 
Space Complexity: O(M + N)
where M and N are the lengths of strings s and t
"""
