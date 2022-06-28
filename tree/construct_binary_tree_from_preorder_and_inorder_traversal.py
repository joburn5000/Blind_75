"""
Given two integer arrays preorder and inorder where preorder is the 
preorder traversal of a binary tree and inorder is the inorder traversal 
of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

Difficulty: Medium
Completed: 6/28/2022
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:           # base case: empty
            return None
        if len(inorder) == 1:           # base case: 1 node
            return TreeNode(inorder[0])
        
        center_index = inorder.index(preorder[0])                                         # index of the center node in the inorder array
        left = self.buildTree(preorder[1:index(center_index+1)], inorder[:center_index])  # recursion: build left node
        right = self.buildTree(preorder[center_index+1:], inorder[center_index+1:])       # recursion: build right node
        return TreeNode(preorder[0], left, right)                                         # construct and return the center node 

"""
Explanation:

We recursively build the tree based on the two arrays.

Base cases are if the arrays are empty or have only 1 element. In those
cases, you'd return None and a single node, respectively

In the recursive case, we create a left and right tree using slices of
the inorder and preorder arrays. We split the arrays based on where the
center node (preorder[0]) is found in the inorder list.

We then create a node that connects the left and right nodes we created.

Time Complexity: O(N)
Space Complexity: O(N)
"""
