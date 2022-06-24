"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?

Difficulty: Medium
Completed: 6/24/2022
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def count_index(head, n):
            i = 0
            if head: 
                i = 1 + count_index(head.next, n)       # if head is not None, then its index is 1 + the index of the next node
            
            if i == n+1:                                # this is the node before the nth node
                head.next = head.next.next              # connect the nodes skipping the nth node
                
            return i
        
        i = count_index(head, n)                        # i stores the total nodes in the list
        if i == n: return head.next                     # i==n means we should remove the head node
        return head

"""
Explanation:

We find the nth node recursively. Then connect the n+1 node to the n-1 node.

Time Complexity: O(N)
Space Complexity: O(N)
"""
