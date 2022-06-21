"""
Given the root of a binary tree, return the level order traversal 
of its nodes' values. (i.e., from left to right, level by level).


Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

Difficulty: Medium
Completed: 6/21/2022
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        def traverse(root, level):
            if not root: return
            if len(output) <= level: output.append([])  # if there is no list for that level yet, create one
            output[level].append(root.val)              # add that node to corresponding list based on level
            traverse(root.left, level+1)                # traverse left child
            traverse(root.right, level+1)               # traverse right child
        traverse(root,0)
        return output

"""
Explanation:

For every level there should be a list that stores the values
of that level. So we create a new list every time we reach a
new level and recursively add values to that list for each level.

Time Complexity: O(N)
Space Complexity: O(N)
"""
