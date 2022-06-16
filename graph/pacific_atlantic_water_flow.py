"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the 
island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix 
heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly 
north, south, east, and west if the neighboring cell's height is less than or equal to the 
current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water 
can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105

Difficulty: Medium
Completed: 5/31/2022

"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        
        # matrix where coast[i][j] is true if value is on a coast
        pacific_coast = [[True if not i or not j else False for j in range(cols)] for i in range(rows)]
        atlantic_coast = [[True if not i or not j else False for j in range(cols)[::-1]] for i in range(rows)[::-1]]
        
        def path_available(x,y,i,j,results,visited):
            if not is_lower_level(x,y,i,j): return False        # out of bounds or higher altitude
            if results[i][j]: return True                       # reached a coast
            if [i,j] in visited: return False                   # already visited
            
            visited.append([i,j])
            if  path_available(i,j,i-1,j,results,visited) or \
                path_available(i,j,i,j-1,results,visited) or \
                path_available(i,j,i+1,j,results,visited) or \
                path_available(i,j,i,j+1,results,visited):      # check paths up, left, down, and right
                results[i][j] = True
            return results[i][j]
        
        
        def is_lower_level(x,y,i,j):
            if x<0 or y<0: return True                      # this just handles the initial case when we start off
            if i >= 0 and i < rows and j >= 0 and j < cols: # check bounds
                return heights[i][j] <= heights[x][y]       # check altitude
            return False
        
        results = []
        for i in range(rows):
            for j in range(cols):
                if path_available(0,-1,i,j,atlantic_coast,[]) and path_available(0,-1,i,j,pacific_coast,[]):    # path to both oceans
                    results.append([i,j])
        
        return results
"""
Explanation:

We use the recursive function path_available to check whther each and every
cell can reach both the Atlantic and Pacific ocean.

Time Complexity: O(N)
Space Complexity: O(N)
"""
