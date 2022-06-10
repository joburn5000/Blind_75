"""

Given an integer n, return an array ans of length n + 1 such that for each i 
(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        memory = {1:1, 0:0}
        
        def numOnes(num):
            if not num in memory:
                if num%2: memory[num] = 1 + numOnes(int(num/2))
                else: memory[num] = numOnes(int(num/2))
            return memory[num]
        
        output = []
        for i in range(n+1):
            output.append(numOnes(i))
            
        return output

"""
Explanation:

The numOnes function counts how many ones are in a digit. It does this by
checking if the value is divisible by 2, then dividing the number by 2 until
it reaches 1 or 0.

We then call the numOnes function from 0 to n inclusive, summing the total
number of ones in all of those digits.

Time Complexity: O(N*log(N))
Space Complexity: O(N)
"""
       
# Faster Solution:

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        
        for i in range(1, n+1):
            ans.append(ans[i // 2] + i%2)      ## using integer division operator.
        
        return ans

"""
Explanation:

We build an array from index 0 to index n that where ans[i] is the number of ones
in ans[i]. The next value of such an array can be calculated using the previous
values in the array, namely ans[i // 2] + i%2.

Time Complexity: O(N)
Space Complexity: O(N)
"""     
