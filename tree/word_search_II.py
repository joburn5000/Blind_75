"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells
are horizontally or vertically neighboring. The same letter cell may not be used more than once 
in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], 
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.

Difficulty: Hard
Completed: 7/5/2022
"""

class TrieNode:
    def __init__(self, char = ""):
        self.char = char
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.end = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # set up the trie
        tree = Trie()
        for word in words:
            tree.insert(word)
        
        
        def search(i,j,node,board, word, output):
            # word is found in our words list
            if node.end: 
                output.append(word)
                # avoid duplicates:
                node.end = False
            
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                # out of range
                return
            
            char = board[i][j]
            node = node.children.get(char)
            if not node:
                return
            # mark as visited
            board[i][j] = "0"
            # search all neighbors
            search(i+1,j,node, board, word+char, output) 
            search(i-1,j,node, board, word+char, output) 
            search(i,j+1,node, board, word+char, output) 
            search(i,j-1,node, board, word+char, output)
            # mark as unvisited
            board[i][j] = char
            
        
        output = []
        # search all values in board
        for i in range(len(board)):
            for j in range(len(board[0])):
                search(i,j,tree.root, board, "", output)
        
        return output

"""
Explanation:

We use the trie class to efficiently search through the nodes
via DFS traversal to find all the matching words. After building
the trie, we recursively search through, updating output as we go.

Time Complexity: O(N*k) where N is the # of values in board and
k is the length of the longest word
Space Complexity: O(N)
"""
