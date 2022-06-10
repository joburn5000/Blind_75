"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

Difficulty: Easy
Completed: 5/29/2022

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        
"""
Explanation: 

A set combines all duplicates. If there are no duplicates, there won't 
be any difference in the length of the set and the original array.

Time Complexity: O(1)
Space Complexity: O(1)
"""
