"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown 
pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], 
nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For 
example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become 
[4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return 
the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

Difficulty: Medium
Completed: 6/18/2022
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        
        if not length: return -1
        if length == 1: return 0 if nums[0] == target else -1
        
        half = int((length-1)/2)
        if nums[-1] > nums[half]:                                   # "turn around" happens in first half
            if nums[half] < target and target <= nums[-1]:              # target in second half
                output = self.search(nums[half+1:], target)
                return -1 if output == -1 else half + 1 + output
            else:                                                       # target in first half
                return self.search(nums[:half+1], target)
        else:                                                       # "turn around" happens in second half
            if target > nums[half] or target <= nums[-1]:               # target in second half
                output = self.search(nums[half+1:], target)
                return -1 if output == -1 else half + 1 + output
            else:                                                       # target in first half
                return self.search(nums[:half+1], target)
                              
"""
Explanation:

The "turn around" is when the values jump down to the lowest value.
This either happens in the first half or second half of the list.

If the turn around is in the first half of the list, then the target
will be in the second half if it is between the midpoint and end values.

If the turn around is in the second half of the list, then the target
will be in the second half if it is greater than the midpoint value or
less or equal to than the end value.

We recursively go through checking these constraints and shortening the
size of the array we are checking by 2 every time until there is 0 or 1
value left. If that value is our target, then we return the index.
Otherwise we return -1.

Time Complexity: O(log(N))
Space Complexity: O(log(N))
"""
