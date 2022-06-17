"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

Difficulty: Medium
Completed: 5/24/2022

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])                      # sort by the starting values
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:       # no overlap
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1]) # overlapping, so change the ending value in the interval
                
        return merged
"""
Explanation:

We go through the (sorted) intervals, and if there is an overlap, we
merge the intervals by changing the ending value of the interval with
the smaller start time.

Time Complexity: O(N)
Space Complexity: O(N)
