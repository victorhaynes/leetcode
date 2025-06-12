class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        For 2 pointer problems give good thought to where the pointers should start...
        that is most the complication,
        along with movement logic
        """
        left = 0
        right = len(height) - 1

        max_area = 0
        while left < right:
            width = right - left
            area = width * min(height[left], height[right]) # else it would spill, need min not max
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1
                # or right -= 1...just move one of them

        return max_area

# Time O(n) at most n total iterations
# Space O(1)