"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

Difficulty: Medium
Completed: 6/15/2022
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        temp = output = 1 if len(nums) else 0
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                temp += 1
            else:
                output = max(output, temp)
                temp = 1
        return max(output, temp)
      
      
"""
Explanation:

We get rid of duplicate values using set(), convert it back to a list using list(),
and then sort using sorted(). This takes O(log(N)) time. Then we check whether
the value at index i+1 is one greater than the value at index i. If so, that value
is consecutive, and we increment the temporary counter temp. If not, we update our
output if temp is greater than our current highest length and we reset temp to 1.
At the end, temp could be higher than output, so we return the highest value between 
temp and output.

Time Complexity: O(N)
Space Complexity: O(1)
"""
