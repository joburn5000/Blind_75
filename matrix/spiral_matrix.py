"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 
Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100


Difficulty: Medium
Completed: 5/26/2022

"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def rotate(row_direction,col_direction):        # rotate by 90 degrees
            if row_direction: return 0,-row_direction   
            if col_direction: return col_direction, 0
        
        def outside_bounds(row,col):                    # check if that row and col is out of bounds
            return row<0 or col<0 or row>=len(matrix) or col>=len(matrix[0]) or matrix[row][col] == "wall"
        
        output = []
        row, col = 0,0
        row_direction, col_direction = 0,1
        while not outside_bounds(row,col):                                          # end if we've rotated and it's still out of bounds
            output.append(matrix[row][col])                                         # add to output
            matrix[row][col] = "wall"                                               # assign entry to a wall
            if outside_bounds(row+row_direction, col+col_direction):                # check next value
                row_direction,col_direction = rotate(row_direction,col_direction)   # rotate if outside bounds
            row += row_direction                                                    # increment row
            col += col_direction                                                    # increment col
        return output
 
"""
Explanation:

This program progresses how a human might: start at top right corner and move to the right.
If we're out of bounds or the next value is one we've already seen (a "wall"), rotate by 90 
degrees and continue until all values have been reached.

Time complexity: O(N*M) where N and M are the row and column lengths
Space complexity: O(N*M)

"""
