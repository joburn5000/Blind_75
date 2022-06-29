"""
You are given an n x n 2D matrix representing an image, 
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you 
have to modify the input 2D matrix directly. DO NOT allocate 
another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

Difficulty: Medium
Completed: 6/29/2022
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        size = len(matrix)
        
        for i in range(int((size+1)/2)):
            for j in range(int(size/2)):
                temp = matrix[i][j]
                matrix[i][j] =  matrix[size-1-j][i]
                matrix[size-1-j][i] = matrix[size-1-i][size-1-j]
                matrix[size-1-i][size-1-j] = matrix[j][size-1-i]
                matrix[j][size-1-i] = temp
        

"""
Explanation:

We look at a quarter of the array, and rotate each value in that
quarter manually.

The bounds for i and j are different as shown above. One is in 
the range of (size+1)/2 and one is in the range size/2 where size 
is the length of the array. They are the same if the length of the
array is even and different if the length of the array is odd.
This is by design. If the length is odd, we want to have a different
bound for the rows and columns. For example, if the length is 3, we
want our quarter to have 2 rows and 1 column. If we had 2 rows and 2
columns, then it would be larger than a quarter and we'd be rotating
some values twice, causing a distortion in the picture.

Time Complexity: O(N)
Space Complexity: O(1)
"""
