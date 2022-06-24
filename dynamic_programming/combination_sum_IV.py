"""
Given an array of distinct integers nums and a target integer target, return 
the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000

Difficulty: Medium
Completed: 6/24/2022
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {0:1}
        
        def recursion(nums, target, cache):
            if target < 0: return 0
            if not target in cache:
                cache[target] = sum(recursion(nums, target - num, cache) for num in nums)
            return cache[target]
        
        return recursion(nums, target, cache)

"""
Explanation:

We store previous results in the dictionary cache, in the format {target: combinations}.
Then we recursively go through each number in the array and sum the possible combinations
reaching the target - num for every num in the array.

Time Complexity: O(N * T)
Space Complexity: O(T)

where N is the number of value in nums and T is the target
"""
