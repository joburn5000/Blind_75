"""
You are given an integer array nums. You are initially positioned 
at the array's first index, and each element in the array represents 
your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the 
last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its 
maximum jump length is 0, which makes it impossible to reach the 
last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105

Difficulty: Medium
Completed: 7/1/2022
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        path = len(nums)-1                      # start at the end of the array
        for i in reversed(range(len(nums)-1)):  # loop through values starting at the second to last value
            if i + nums[i] >= path:             # if current nums[i] value can reach the path
                path = i                        # update the path
        return path == 0                        # if path == 0 then index 0 has a path to the end

"""
Explanation:

We store the smallest index where there is a path
to the end called "path." For every index starting
with the second to last, if that index can reach
path (its value + its index is greater than or equal
to path), then that index will be the new smallest
indes. At the end, if path is 0, then there is a path
from index 0 to the end.

Time Complexity: O(N)
Space Complexity: O(1)
"""
