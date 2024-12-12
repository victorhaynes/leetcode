from typing import List
"""
URL: https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 
Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""

# Optimal
# O(n) time O(1) space
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # edge cases
        if len(flowerbed) == 1:
            if flowerbed == [0] and n == 1:
                return True
            elif flowerbed == [0] and n > 1:
                return False
            elif flowerbed == [0] and n == 0:
                return True
            elif flowerbed == [1] and n == 0:
                return True
            elif flowerbed == [1] and n != 0:
                return False
        
        # main lgorithm
        last_index = len(flowerbed) - 1
        for i, bed in enumerate(flowerbed):
            if bed == 1: # if flower, skip
                continue
            elif i == 0 and flowerbed[i+1] == 0: # if on first bed, and spot to the right is empty
                n -= 1
                flowerbed[i] = 1
            elif i == last_index and flowerbed[i-1] == 0: # if on last bed, and spot to the left is empty
                n -= 1
                flowerbed[i] = 1
            elif bed == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
        
        print(flowerbed)
        if n > 0:
            return False
        else:
            return True