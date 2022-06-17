"""

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by 
starti. You are also given an interval newInterval = [start, end] that represents the start and 
end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti 
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105

Difficulty: Medium
Completed: 5/14/2022

"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        preceding = []
        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0]: # (1)
                # find the left bound of our merged interval
                starting_value = newInterval[0] if newInterval[0] < intervals[i][0] else intervals[i][0]
            
                # now find the right bound
                for index in range(i,len(intervals)):
                    if intervals[index][0] > newInterval[1]:
                        return preceding + [[starting_value,newInterval[1]]] + intervals[index:] # 4
                    elif intervals[index][1] >= newInterval[1]:
                        return preceding + [[starting_value,intervals[index][1]]] + intervals[index+1:] # 5
                      
                        # key: preceding + merged + following intervals
                    
                return preceding + [[starting_value,newInterval[1]]] # 6
            
            else:
                preceding.append([intervals[i][0], intervals[i][1]]) # (2) intervals before the new interval
                
        return preceding + [newInterval] # 7
      
      
      
"""
Explanation:

Loop through the intervals, checking if the new interval is within any of their bounds (1). 

As you go, append each of these non-overlapping intervals to "preceding" (2). Once a match is found, 
the starting value (3) is the min of newInterval[0] and intervals[i][0] where i is the location of 
your first overlapping interval. 

Then loop through the remaining intervals. If it newInterval[1] is just before a bound, do not include 
that bound in merged (4). If the newInterval[1] is within the bounds, merge using the interval bound 
(5). If that interval is outside the bounds,  there will be no future intervals to consider (6). If 
the new interval is completely to the right of all the other bounds, then just return preceding plus 
newInterval (7). This covers all possible cases.

Time Complexity: O(N*log(N))
Space Complexity: O(N)

"""
      
      
      
      
      
