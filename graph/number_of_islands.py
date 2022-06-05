"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

Difficulty: Medium
Completed: 5/4/2022

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        def is_land(row,col):
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0: return False  # row and col are out of bounds
            return grid[row][col] == "1"                                                    # true if "1" and false otherwise
        
        def turn_water(row,col):
            grid[row][col] = "0"                          # change to water
            if is_land(row+1,col): turn_water(row+1,col)  # check down
            if is_land(row-1,col): turn_water(row-1,col)  # check up
            if is_land(row,col+1): turn_water(row,col+1)  # check right
            if is_land(row,col-1): turn_water(row,col-1)  # check left
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if is_land(i,j):          # liquidate every island we find
                    count += 1
                    turn_water(i,j)
        
        return count
"""
Explanation:

When we find a piece of land, we increment the count and "sink" the whole island
by changing all neighboring "1"s to "0"s recursively. We then continue the search
for each remaining grid.


"""
