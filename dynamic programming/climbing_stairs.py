"""
Climbing Stairs
Difficulty: Easy

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct 
ways can you climb to the top?

 
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45


"""

class Solution:
  
    # brute force method: recursion
    
    # base case: 0 or 1 step = 1 way
    # recursive step: example 2: either;
        #    2 steps: 0 left
        #    1 step: 1 left
    
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-2) + self.climbStairs(n-1)
      
      
      
    # dynamic programming method: fibonacci
    
    def fibonacci(self, n:int) -> int:
        num = [1,0]
        for i in range(n):
            temp = num[0]
            num[0] = num[0]+num[1]
            num[1] = temp
        return num[0]
    
    def climbStairs(self, n: int) -> int:
        return self.fibonacci(n)
    
 
            
