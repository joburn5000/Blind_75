"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

Difficulty: Medium
Completed: 6/8/2022
"""

# dp method:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        minimum = output = nums[0]
        sums = [output]
        
        for i in range(len(nums)):
            sums.append(sums[i]+nums[i])              # add current sum to array
            output = max(sums[i+1] - minimum, output) # update output if necessary
            minimum = min(minimum, sums[i+1])         # update minimum if necessary
                
        return output

"""
Explanation:

sums is an array where sums[i] has the sum of the values from indexes 0 to i (inclusive)
using this array, we can find the sum of all numbers between i and j (inclusive) = sums[i]-sums[j]

minimum is a value that has the smallest sum so far
the greatest sum including index i will be sums[i]-minimum. if this sum is the highest we've ever seen, update output

Time Complexity: O(N)

"""

class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        
        temp_sum = biggest_sum = nums[0]
        for element in nums[1:]:
            temp_sum = max(element, temp_sum+element)
            biggest_sum = max(temp_sum, biggest_sum)
        return biggest_sum
"""
Explanation:

we loop through the array keeping track of the temp_sum and biggest_sum

temp sum gets updated when it is more advantageous to forget about all values seen so far
and start anew with the new value we have. this happens when temp_sum < 0 and temp_sum < element

biggest sum gets updated if temp_sum is ever bigger than temp_sum

Time Complexity: O(N)
Space Complexity: O(1)
"""
