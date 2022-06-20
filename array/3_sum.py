"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

Difficulty: Medium
Completed: 6/20/2022
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for left in range(len(nums)-2):
            if left > 0 and nums[left] == nums[left-1]:     # checks for duplicates
                continue
            mid, right = left+1, len(nums)-1
            while mid < right:
                s = nums[left] + nums[mid] + nums[right]                # s is the sum of the numbers
                if s < 0:                                               # s is too small so increase the mid pointer
                    mid += 1
                elif s > 0:                                             # s is too large so decrease the right pointer
                    right -= 1
                else:                                                   # s is 0
                    answer.append([nums[left], nums[mid], nums[right]]) # add numbers to answer
                    while mid < right and nums[mid] == nums[mid+1]:     # get rid of recurring values for mid pointer
                        mid += 1
                    while mid < right and nums[right] == nums[right-1]: # get rid of recurring values for right pointer
                        right -= 1
                    mid += 1; right -= 1                                # move pointers
                    
"""
Explanation:

We sort the array, then for each number, check the values
after that number for a sum to 0.

We accomplish this by having pointers move according to 
whether the sum is greater than, less than, or equal to 0.

Time Complexity: (O(N^2))
Space Complexity: O(N)

"""
