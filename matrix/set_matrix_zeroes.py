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
Completed: 5/16/2022

"""

# O(n) solution using numpy

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
      
# note: this solution is not "in-place" as it requires transforming the 
#       data into an auxiliary data structure (numpy array)
