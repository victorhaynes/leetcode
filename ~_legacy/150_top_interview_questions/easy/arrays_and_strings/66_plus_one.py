from typing import List
"""
URL: https://leetcode.com/problems/plus-one/description/
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

# Optimal
# remember backwards iteration syntax
# for i in range(len(digits) - 1, -1, -1):
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):
            # Increment the current digit
            digits[i] += 1
            # If it becomes 10, set it to 0 and continue to the next digit
            if digits[i] == 10: 
                digits[i] = 0
            else: 
                # No carry, so we can return early
                return digits
        
        # If we finished the loop, all digits were 9, so prepend a 1
        return [1] + digits


# Intution, near optimal
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1] # reverse the array

        for i,d in enumerate(digits):
            if i == 0:
                digits[0] = digits[0] + 1
            if digits[i] == 10:
                digits[i] = 0
                try:
                    digits[i+1] = digits[i+1] + 1
                except IndexError: # If you can't add to the next index in the array it doesn't exist, and mathematically it would have be to 10 -> [0,1] so append 1 to the end of list
                    digits.append(1)
            

        return digits[::-1] # re-reverse list and return it
# time O(n) - one iteration through n digits
# space O(n) - reversing the the digits array takes n space