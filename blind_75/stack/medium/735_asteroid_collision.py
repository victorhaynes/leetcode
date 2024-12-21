"""
URL: https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75

We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

"""
from typing import List

# Optimal - needed help
# Time O(n) - for loop n times - operations done inside the loop are proportional to n bc they can only be done once (not n times on each iteraiton) --- so O(n)
# Space O(n) - stack of size n

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for a in asteroids:
            
            # will skip first iteration, stack is falsey
            while stack and a < 0 < stack[-1]:
                if abs(a) < abs(stack[-1]):
                    break # do not add a (asteroid) - break and go to next a
                elif abs(a) > abs(stack[-1]):
                    stack.pop() # and continue, bc it may need to destroy the next asteroid in the stack - go to next while iteration, may pass/my fail
                elif abs(a) == abs(stack[-1]):
                    stack.pop() # destroy asteroid in stack, do not add a
                    break
                else:
                    raise Exception
            
            else:
                stack.append(a)


        return stack