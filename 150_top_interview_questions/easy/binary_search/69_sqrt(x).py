"""
URL: https://leetcode.com/problems/sqrtx/description/

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""

# Optimal
# Time O(logn)
# Space O(1)
# Takeaways: calculate mid as left + (right-left)/2 or use //2 if we are dealing with whole numbers only like an integer or an index
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        result = 0

        while left <= right:
            mid = left + (right - left)//2 # use // to do interger division, removes all decimals like math.floor(n)
            # could just do m = (left + right)/2 in python as you won't have overflow issues in this language
            if mid**2 > x:
                right = mid - 1
            elif mid**2 < x:
                left = mid + 1
                result = mid
            else: # middle**2 == x:
                return mid

        return result