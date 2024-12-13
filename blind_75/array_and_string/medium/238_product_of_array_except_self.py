from typing import List
"""
URL: https://leetcode.com/problems/product-of-array-except-self/description/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

 
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""

# Given a hint, here is my optimal solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        left = [] # append a prefix product looking at everything to the left of postition i
        right = [] # append a prefix product looking at everything to the right of position i (starting at the end of nums...this will need to reversed)
        left_prefix_product = 1
        right_prefix_product = 1

        for i,n in enumerate(nums):
            if i == 0:
                left_prefix_product *= 1
            else:
                left_prefix_product *= nums[i-1] # this works as expected here for left
            left.append(left_prefix_product)
        # print(left)

        i = len(nums) - 1
        while i >= 0:
            if i == len(nums) - 1:
                right_prefix_product *= 1
            else:
                right_prefix_product *= nums[i+1] # for the right array we populate it from the last index up until the 1st index, so it needs to be reversed later
            right.append(right_prefix_product)
            i -= 1
        # print(right)

        right = list(reversed(right))

        for i,n in enumerate(nums):
            answer.append(left[i]*right[i])

        return answer



        # # youtube optimal solution: https://www.youtube.com/watch?v=yKZFurr4GQA
        # to_left_prefix_product = 1
        # to_right_prefix_product = 1
        # n = len(nums)
        # left_list = [0] * n
        # right_list = [0] * n

        # for i in range(n): # Remember range will give you 0 indexed list & n is exclusive... n = 3 -> range(n) = [0,1,2]
        #     j = -i -1 # this is how you get a pointer that moves opposite of i in a for loop
        #     left_list[i] = to_left_prefix_product
        #     right_list[j] = to_right_prefix_product
        #     to_left_prefix_product *= nums[i]
        #     to_right_prefix_product *= nums[j]

        # return [l*r for l,r in zip(left_list, right_list)]




        # BRUTE FORCE: O(n) / approach that is easy to see:
        # answer = []
        # i,j = 0, 0
        # while i < len(nums):
        #     product = 1
        #     while j < len(nums):
        #         if i != j:
        #             product *= nums[j]
        #         j += 1
        #     answer.append(product)
        #     i += 1
        #     j = 0

        # return answer