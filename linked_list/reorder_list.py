"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Difficulty: Medium
Completed: 6/26/2022
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:        
        def recursion(left, right):
            if not right:                       # end of the list
                return left
            left = recursion(left, right.next)  # recursion step
            
            if not left:                                  # base case: our left node is null
                return None
            
            if left == right or left.next == right:       # base case: we are in the middle of the list
                right.next = None                         # right is the final node; right.next is null
                return None
            else:
                left.next, right.next = right, left.next  # connect the nodes according to directions
                return right.next
        return recursion(head, head.next)
            

"""
Explanation:

Using recursion, we connect the nodes in the order described.

Here is an animation of the algorithm: 

https://docs.google.com/presentation/d/e/2PACX-1vQ-Oy-oQ0i4CvWbo8gf9-v42gVOb5gS76sJvhG7jqIntQV7R1dDG3tS7YUhRiPqYXBCjqCcVsJUeZjG/pub?start=true&loop=false&delayms=1500&slide=id.gbc95359713_0_20

Time Complexity: O(N)
Space Complexity: O(1)
"""
"""        
class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
      # Do not return anything, modify head in-place instead

      nums = []
      temp = head
      while temp:
          nums.append(temp.val)
          temp = temp.next
      temp = head
      for i,num in enumerate(nums):
          temp.val = nums[len(nums)-1-int(i/2)] if i%2 else nums[int(i/2)]
          temp = temp.next  
"""
"""
Explanation:

Simpler but less space efficient and less elegant. We make an array with nums
and then change the values of the nodes based on the order described. It also
requires 2 passes

Time Complexity: O(N)
Space Complexity: O(N)
"""
