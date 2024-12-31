"""
URL: https://leetcode.com/problems/plus-one/

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""
from typing import List

# Optimal - self
# Time O(n)
# Space O(1) - why? modifying digits in place (O)1....input array digits does not count O(1)....and transient operation like the return [1] + digits doesn't count
# the return takes O(n) time to build but it isn't held in memory

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if len(digits) == 1:
            if digits[0] == 9:
                return [1,0]
            else:
                return [digits[0]+1]

        
        if digits[-1] == 9:
            carry = 1
            digits[-1] = 0
        else:
            carry = 0
            digits[-1] += 1
            return digits

        for i in range(len(digits) -1,-1,-1):
            if i == len(digits) -1:
                continue # skip first digit from the right, handled outside of loop
            if carry:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                return digits

        if carry:
            digits[0] = 0
            return [1] + digits
        else:
            return digits