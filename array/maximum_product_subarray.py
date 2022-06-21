"""
Given an integer array nums, find a contiguous non-empty subarray within the 
array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
Accepted
772,487
Submissions
2,229,736

Difficulty: Medium
Completed: 5/20/2022
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maximum = minimum = highest = nums[0]
        
        for num in nums[1:]:
            # if the number is negative the largest and smallest values swap
            if num < 0:                     
                minimum, maximum = maximum, minimum # swap
            
            # choose whether to start afresh with the new
            maximum = max(num, num*maximum)
            minimum = min(num, num*minimum)
            
            # update highest if necessary
            highest = max(highest, maximum)
        
        return highest
      
"""
Explanation:

We save the running maximum and minimum values, because the
minimum number so far could become the maximum if it is multiplied
by a negative number.

Time Complexity: O(N)
Space Complexity: O(1)
"""
