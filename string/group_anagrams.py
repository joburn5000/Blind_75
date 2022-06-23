"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original 
letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

Difficulty: Medium
Completed: 6/23/2022
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [''.join(sorted(x)) for x in strs]    # list of sorted strings
        anagrams = {key: [] for key in set(sorted_strs)}    # dictionary where each key is an unique anagram
        for i, s in enumerate(strs):                        
            anagrams[sorted_strs[i]].append(s)              # the values of the dictionary are the anagrams of the key
        return [val for val in anagrams.values()]           # return a list made from the values of the dictionary

"""
Explanation:

We sort the strings, then group the sorted strings
together (those are anagrams), and return a list
with the grouped anagrams.

Time Complexity: O(N)
Space Complexity: O(N)
"""
