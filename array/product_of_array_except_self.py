"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Difficulty: Medium
Completed: 6/3/2022

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1: return [0]*len(nums)                                  # more than 1 zero, return all zeroes
        total = prod(nums)                                                          # total including the 0
        total_without_zero = prod([num for num in nums if num])                     # total excluding the 0 
        return [total_without_zero if not num else int(total/num) for num in nums]  # return non_zero total if num is 0, else return the total/that number
