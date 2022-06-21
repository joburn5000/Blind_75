"""
Given the roots of two binary trees root and subRoot, return true 
if there is a subtree of root with the same structure and node 
values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node 
in tree and all of this node's descendants. The tree tree could 
also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

Difficulty: Easy
Completed: 6/21/2022
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self, root, subRoot):                         # checks two trees for sameness
        if not (root and subRoot): return root == subRoot   # one or both of the nodes are NULL
        return root.val == subRoot.val and \
                self.check(root.left, subRoot.left) and \
                self.check(root.right, subRoot.right)       # check that node values and children are the same

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not (root and subRoot): return root == subRoot   # one or both of the nodes are NULL                      
        if self.check(root, subRoot): return True           # call the check function
        return self.isSubtree(root.left, subRoot) or \
                self.isSubtree(root.right, subRoot)         # see if there's a match for either child

"""
Explanation:

The check function checks for sameness for two nodes.

We first check the root node for sameness with the subtree
node. If we find that those are unidentical, we move on to
check the children of the root.

Time Complexity: O(N)
Space Complexity: O(1)
"""
