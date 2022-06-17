"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes 
in the sequence has an edge connecting them. A node can only appear in the sequence 
at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Difficulty: Medium
Completed: 6/8/2022
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        output = [-100000]
        
        def recurse(root):
            if not root: return 0
            center, left, right = root.val, recurse(root.left), recurse(root.right)
            possible_max = max(center, center+left, center+right, center+left+right)
            if possible_max > output[0]: output[0] = possible_max
            return max(root.val, root.val + left, root.val + right)
        
        recurse(root)
        
        return output[0]
"""
Explanation:

At any level, the maximum possible sum is the either just the center val,
the center val + right max sum, the center val + left max sum, or the 
center val + right max sum + left max sum.

We recursively check all these possibilities, and output the highest.

Time Complexity: O(N)
Space Complexity: O(N)
"""
