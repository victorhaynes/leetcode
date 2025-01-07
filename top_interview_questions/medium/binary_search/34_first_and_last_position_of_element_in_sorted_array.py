"""
URL:

"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first_occurence = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first_occurence = mid
                    right = mid - 1  # Search the left half for earlier occurrences
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first_occurence

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last_occurence = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last_occurence = mid
                    left = mid + 1  # Search the right half for later occurrences
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last_occurence

        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]
