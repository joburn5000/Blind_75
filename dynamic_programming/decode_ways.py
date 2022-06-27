"""
A message containing letters from A-Z can be encoded into numbers 
using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then 
mapped back into letters using the reverse of the mapping above 
(there may be multiple ways). For example, "11106" can be mapped 
into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot 
be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways 
to decode it.

The test cases are generated so that the answer fits in a 32-bit 
integer.

Difficulty: Medium
Completed: 6/27/2022
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0                  # strings starting with a 0 have 0 ways to decode
        
        output = [1,0]                            # number of ways for [right 1 to the end, right 2 to the end]
        prev = ""                                 # previous character
        
        for char in s[::-1]:
            temp = output[0]                      # temp will go into output[1] aka # of ways for 2 to the right to the end
            if 0 < int(char+prev) < 27:           # the combination of the last 2 strings is within the bounds
                if char == "0":     
                    temp = output[1]              # keep output[1] the same
                elif prev != "0" and prev != "":  # if prev is "0" or "" there are the same # of ways as before
                    output[0] = sum(output)       # otherwise, the # of ways are the sum of the output[0] and outpu[1]
            elif prev == "0":
                return 0                          # this happens if there is every 00, 30, 40, 50 etc., in which there are 0 ways
            
            output[1] = temp                      # shift
            prev = "" if prev == "0" else char    # update prev
        
        return output[0]
           

"""
Explanation:

This problem requires some hard coding of cases, since there
is a special rule about 01, 02, 03, etc. not being able to count
as a valid encoding.

We loop through and for index i in the string, output[0] stores
the number of ways to decode s[i+1:] and output[1] stores the number 
of ways to decode s[i+2:]. Then if the critia is met (there are
ways of ordering a new string based on the s[i] and prev) then the
value is the sum of the output.

At the end, output[0] stores the number of ways to decode s

Time Complexity: O(N)
Space Complexity: O(1)
"""
