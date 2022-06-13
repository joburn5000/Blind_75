"""
uppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.

Difficulty: Medium
Completed: 6/13/2022
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 2: 
            return nums[0] if nums[0] < nums[1] else nums[1]    # base case: return smaller of the 2
        if len(nums) == 1: 
            return nums[0]                                      # base case: return single entry
        
        if nums[-1] < nums[int(len(nums)/2)]:
            return self.findMin(nums[int(len(nums)/2)+1:])      # smallest value is in the second half of list
        else: 
            return self.findMin(nums[:int(len(nums)/2)+1])      # smallest value is in the first half of list
"""
Explanation:

We take a look at the midpoint and the final value. If the final 
value is less than the midpoint value, then we know that the
smallest value will be found in the second half of the list, not
including the midpoint value. Otherwise, we know that the samllest
value is found in the first half of the list, including the midpoint
value.

Time Complexity: O(log(N))
Space Complexity: O(1)
"""
