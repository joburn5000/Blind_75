"""
You are given an integer array height of length n. There are n 
vertical lines drawn such that the two endpoints of the ith line 
are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array 
[1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue 
section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
Accepted
1,558,643
Submissions
2,883,977

Difficulty: Medium
Completed: 6/22/2022
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        res = 0
        while left < right:
            res = max(res, (right-left)*min(height[left], height[right])) # update the result if necessary
            if height[left] < height[right]:                              # right height is greater than left left height
                left += 1                                                 # increment left pointer
            else:                                                         # left height is greater than or equal to right height
                right -= 1                                                # decrememt right pointer
        return res

"""
Explanation:

We use 2 pointers: left and right, and move whichever
height is the smaller of the two closer, updating the
result if we find an area that is greater than before

Time Complexity: O(N)
Space Complexity: O(1)
"""
