"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have 
security systems connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each 
house, return the maximum amount of money you can rob tonight without 
alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

Difficulty: Medium
Completed: 6/26/2022
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        choices = [0,0,0]
        for num in nums:
            choices[0], choices[1], choices[2] = choices[1], choices[2], max(num+choices[0], num+choices[1], choices[2])
        return choices[2] if choices[2] > choices[1] else choices[1]

"""
Explanation:

At any given house, the robber has the following options:
- Rob the current house and the house 3 to the left
- Rob the current house and the house 2 to the left
- Rob the house 1 to the left

The array "choices" stores those options, starting from the
first house on the left. We loop through all the numbers,
keeping track of how much money each house could gain, including
all the houses to its left. We calculate the max amount of money
for a new house, and then shift all the values to the left.

After looping through all the nums, the total will be the bigger
between the last and second-to-last house.

Time Complexity: O(N)
Space Complexity: O(1)
"""
