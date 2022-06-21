"""
Given an integer array nums and an integer k, return the k most 
frequent elements. You may return the answer in any order.


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than 
O(n log n), where n is the array's size.

Difficulty: Medium
Completed: 6/20/2022
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for x in range(len(nums) + 1)]
        c = Counter(nums).items()  
        for num, freq in c: bucket[freq].append(num) 
        flat_list = list(chain(*bucket))
        return flat_list[::-1][:k]

"""
Explanation:

We create empty buckets and assign the value of bucket[i]
to be the the value x where there are i instances of x in
nums. Then we flatten the bucket into one giant list and
return the top k instances.

Time Complexity: O(N)
Space Complexity: O(N)
"""
