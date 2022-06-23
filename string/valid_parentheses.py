"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

Difficulty: Medium
Completed: 6/22/2022
"""

class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {'(':')', 
                      '[':']', 
                      '{':'}'}
        stack = " "
        for letter in s:
            if not stack[-1] in dictionary or letter != dictionary[stack[-1]]: 
                stack += letter
            else:
                stack = stack[:-1]
        return stack == " "

"""
Explanation:

We use a stack to keep track of letters. If the top of the stack
is the opening character for the next letter, we pop both of those
off of the stack. If the string is "valid" then it will be the empty.

Time Complexity: O(N)
Space Complexity: O(N)
"""
