"""
Given an m x n grid of characters board and a string word, 
return true if word exists in the grid.

The word can be constructed from letters of sequentially 
adjacent cells, where adjacent cells are horizontally or 
vertically neighboring. The same letter cell may not be 
used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Difficulty: Medium
Completed: 7/2/2022
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recursion(i,j,board,word):
            # if the word is "" then it IS found in the board
            if not word:    
                return True
            
            # checks that i & j are within bounds and the letter at [i][j] is the correct letter
            if not (i >= 0 and j >= 0 and i < len(board) and j < len(board[0]) and board[i][j] == word[0]): 
                return False
            
            # temporarily set the letter at [i][j] to "0" for "visited"
            temp = board[i][j]
            board[i][j] = "0"
            
            # traverse neighboring letters
            output =    recursion(i+1,j,board,word[1:]) or \
                        recursion(i-1,j,board,word[1:]) or \
                        recursion(i,j+1,board,word[1:]) or \
                        recursion(i,j-1,board,word[1:])
            
            # set the letter at [i][j] back to its original value
            board[i][j] = temp
            
            # true if we found the word in the board
            return output
        
        # loop through all the values to find a match
        for i in range(len(board)):
            for j in range(len(board[0])):
                if recursion(i,j,board,word): 
                    return True
        
        return False

"""
Explanation:

We use a DFS traversal to check if there is a match for
the given word in our array.

Time Complexity: O(N)
Space Complexity: O(N)
"""
