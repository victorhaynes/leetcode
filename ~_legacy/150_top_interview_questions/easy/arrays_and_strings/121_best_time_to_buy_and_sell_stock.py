# Time: O(n) -> right pointer moves n times
# Space: O(1) -> constant space

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        max_profit = 0
        left = 0 # past date
        for right in range(len(prices)): # future date
            if right == 0:
                continue
            
            if prices[right] <= prices[left]:
                left = right
            else:
                max_profit = max(max_profit, prices[right] - prices[left])

        return max_profit
