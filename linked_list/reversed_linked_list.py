"""

Given the head of a singly linked list, reverse the list, and return the reversed list.

 
Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


Difficulty: Easy
Completed: 5/15/2022

"""


# iterative solution:

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        
        # add values to a list
        curr_node = head
        while curr_node:
            nodes.append(curr_node.val)
            curr_node = curr_node.next
        
        # put reversed values in
        curr_node = head
        for value in nodes[::-1]:
            curr_node.val = value
            curr_node = curr_node.next
            
        return head
      
# recursion:

class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head            # edge case (empty list)
        
        def recursion(curr, before):
            temp = curr.next                # save as temporary variable
            curr.next = before              # reverse each node
            
            if temp == None:                # base case: you are at the last node
                return curr                 # the last node will become the first
            
            return recursion(temp, curr)    # recursion: reverse the next node
        
        return recursion(head, None)
