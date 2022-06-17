"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

Difficulty: Easy
Completed: 5/18/2022

"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0                                                         # base case: null node
        else: return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))     # recursion step: choose max length beween right and left
     
"""
Explanation: 

We use BFS recursion, choosing to return 1 plus the greater value of the left depth
and the right depth for every non-NULL root

Time Complexity: O(N)
Space Complexity: O(1)
"""
