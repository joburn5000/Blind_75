"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this 
place are arranged in a circle. That means the first house is the 
neighbor of the last one. Meanwhile, adjacent houses have a security 
system connected, and it will automatically contact the police if two 
adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each 
house, return the maximum amount of money you can rob tonight without 
alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000

Difficulty: Medium
Completed: 6/27/2022
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        def line_rob(nums):
            choices = [0,0,0]
            for num in nums:
                choices[0], choices[1], choices[2] = choices[1], choices[2], max(num+choices[0], num+choices[1], choices[2])
            return choices[2] if choices[2] > choices[1] else choices[1]
        
        if len(nums) == 1: return nums[0]
        
        include_first = line_rob(nums[:-1])
        exclude_first = line_rob(nums[1:])
        
        return max(include_first, exclude_first)
        

"""
Explanation:

This problem is almost identical to house_robber.py and uses copied code
inside the "line_rob" function.

We can break the circle into 2 possible lines. We can either include the
first house and exclude the last house, or include the last house and 
exclude the first house. We return the maximum of those 2

Time Complexity: O(N)
Space Complexity: O(1)
"""
