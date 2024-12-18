from typing import List
"""
URL: https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

"""

# Optimal
# Time O(n) - iterating through g once
# Space O(1) - number or size of variables do not scale with the input size
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        max_altitude = 0

        for g in gain:
            current_altitude += g
            max_altitude = max(current_altitude, max_altitude)


        return max_altitude