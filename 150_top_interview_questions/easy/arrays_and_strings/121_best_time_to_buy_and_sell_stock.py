"""
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
from typing import List


# Optimal, make sure the left pointer index after initialization always represents a lower price than the right pointer index
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 # Buy
        right = 1 # Sell
        max_profit = 0
        while right < len(prices):
            current_profit = prices[right] - prices[left]
            max_profit = max(max_profit, current_profit)
            if prices[right] < prices[left]:
                left = right # if the price went down move the left pointer to the new lower price
            right += 1 # slide along until you run out of days
        return max_profit
# time O(n)
# space O(1)


# Brute force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, price in enumerate(prices):
            j = i + 1
            while j < len(prices):
                bought = price
                sold = prices[j]
                max_profit = max(max_profit, sold - bought)
                j+=1
        return max_profit