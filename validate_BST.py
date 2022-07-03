"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

Difficulty: Medium
Completed: 7/3/2022
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, lowest, highest):
            if not root: return True
            if root.val >= highest or root.val <= lowest: return False
            return check(root.left, lowest, root.val) and check(root.right, root.val, highest)
        
        return check(root, float('-inf'), float('inf'))

"""
Explanation:

We keep track of the lowest and highest values, the bounds for a given node. 

When we traverse left, the lower bound stays the same and the higher bound
becomes that node's value.

When we traverse right, the higher bound stays the same and the lower bound
becomes that node's value.

If none of the nodes are outside of the given bounds, then it is a valid BST.

Time Complexity: O(N)
Space Complexity: O(1)
"""
