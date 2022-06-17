"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Difficulty: Medium
Completed: 5/17/2022

"""

# numpy solution:

import numpy as np

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        matrix = np.array(matrix)
        copy = matrix.copy()
        rows, cols = len(matrix), len(matrix[0])
        bigger = max(rows,cols)
        
        for i in range(bigger):
            if 0 in copy[i % rows]:
                matrix[i % rows] = 0
            if 0 in copy[:, i % cols]:
                matrix[:,i % cols] = 0
                
        return matrix

       """
Explanation:

We transform the data into a numpy array, where we
can easily check whether 0 is found in the row or
column for all the rows and columns.

note: this solution is not "in-place" as it requires 
transforming the data into an auxiliary data structure

Time Complexity: O(N)
Space Complexity: O(N)
"""


# O(1) space complexity solution:

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col = False
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            if matrix[i][0] == 0:
                is_col = True

            for j in range(1,cols):
                # if an element is 0, set corresponding row and column to 0
                
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1,rows):     
            for j in range(1,cols):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0                            # update elements
        
        if matrix[0][0] == 0:                                   # check first row
            for j in range(cols):
                matrix[0][j] = 0
        
        if is_col:                                              # check first column
            for i in range(rows):
                matrix[i][0] = 0
"""
Explanation:

This algorithm uses row 0 and column 0 as storage variables, indicating whether there is
a 0 in that row or column. Since there are n rows and n columns but only n+m-1 places in
column 0 and row 0 combined, we use an extra variable, is_col, to store the final info.

We use these placeholders to update the array in place, as shown by the comments.

Time Complexity: O(N)
Space Complexity: O(1)
"""
