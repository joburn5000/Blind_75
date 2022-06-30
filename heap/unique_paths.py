"""
There is a robot on an m x n grid. The robot is initially located 
at the top-left corner (i.e., grid[0][0]). The robot tries to move 
to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot 
can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique 
paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or 
equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100

Difficulty: Medium
Completed: 6/30/2022
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for row in range(n+1)] for col in range(m+1)] # extra row and col full of 0s for a cushion
        paths[m][n-1] = 1                                         # will produce 1 way to get to the desination from the destination
        
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                paths[i][j] = paths[i+1][j] + paths[i][j+1]       # ways by going down + ways by going right
        
        return paths[0][0]
                 

"""
Explanation:

For any given square, the number of ways to get to the bottom-right
corner are the number of ways by going to the right plus the number
of ways going down. 

We start from the bottom right corner (where the number of ways is 1)
and work our way to the top left corner, keeping track of the values.

Time Complexity: O(N)
Space Complexity: O(N)
"""
