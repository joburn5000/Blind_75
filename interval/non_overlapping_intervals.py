"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum 
number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104

Difficulty: Medium
Completed: 5/12/2022
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        prev = float("-inf")
        ans = 0
        for i in intervals:
            if i[0] >= prev:
                prev = i[1]
            else:
                ans += 1
        return ans
      
      
"""
Explanation:

We start by sorting the intervals by their end value. Then we keep track of the biggest non-deleted
end time and store it in "prev" which starts and -inf. For each interval, if its start time is less
than prev, we'll "delete" it, increasing our answer by 1. If we are to keep the interval, we update
prev to be that inteval's end time. 

This works because the end times are strictly increasing due to how we sorted the intervals, and we 
always want to delete the interval with the higher end time because that has opportunity to overlap 
with more intervals.

Time Complexity: O(N*log(N))
Space Complexity: O(1)
"""
