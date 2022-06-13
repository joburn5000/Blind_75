"""

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
