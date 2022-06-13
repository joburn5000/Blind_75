"""
Given a string s and a dictionary of strings wordDict, return true if s can be 
segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the 
segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

Difficulty: Medium
Completed: 6/13/2022
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = []
        def recursion(string,cache):
            if len(string) == 0: return True
            if string in cache: return False
            for word in wordDict:
                length = len(word)
                if string[:length] == word:
                    if recursion(string[length:], cache): return True
            cache.append(string)
            return False
        return recursion(s,cache)
      
"""
Explanation:

The "recursion" function checks whether the the first letters of the string
can be formed into one of the words in our dictionary. If not, we add that
string to a "cache" array that holds all strings that cannot be formed into
words. If a word can be used, we call on the recursion function using all letters
after that word. If it turns out that this word can evenly break up the string,
we return true. If not, we move on to the next word until there are no more words
left. Cache helps to avoid repition in our calculation. By saving all strings that
don't work, we can avoid redundant calculations.

Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""
