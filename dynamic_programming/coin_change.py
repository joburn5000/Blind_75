"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

Difficulty: Medium
Completed: 5/22/2022

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def recursion(num, cache):
            if num < 0: return 10001            # base case: number is negative (impossible, return high number)
            if num == 0: return 0               # base case: number is 0 (exactly 1 coin left)
            if num in cache: return cache[num]  # base case: number has already been seen
            
            cache[num] = min(recursion(num-coin, cache) + 1 for coin in coins)  # recursion step: find smallest coin number 
                                                                                # and add this entry to cache 
            return cache[num]                                                   # return this entry
        
        output = recursion(amount, {})          # perform recursion
        if output > 10000: return -1            # if case is impossible, it will be an impossbly high number
        else: return output
        
"""
Explanation:

We recursively find the smallest number of coins, using a cache system
to eliminate repetitions in the calculations.

Time Complexity: O(N*M)
Space Complexity: O(M)
"""
