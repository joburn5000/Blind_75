# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = output = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                # list1 contains smaller value
                curr.next = list1
                list1 = list1.next
            else: 
                # list2 contains smaller value
                curr.next = list2
                list2 = list2.next
            # increment the curr pointer
            curr = curr.next
            
        if list1 or list2:
            # add any remaining values to the end of our list
            curr.next = list1 if list1 else list2
        
        # we return output.next instead of output because output was just a dummy node.
        # the real start of the list we care about is at output.next
        return output.next
  
  """
  Explanation:
  
  We add the smaller value of the two lists until there is only 1 list remaining (or 0).
  
  Time Complexity: O(N)
  Space Complexity: O(1)
  
  """
