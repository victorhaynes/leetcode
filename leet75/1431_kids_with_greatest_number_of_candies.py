class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)

        for i,c in enumerate(candies):
            if c + extraCandies >= greatest:
                candies[i] = True
            else:
                candies[i] = False

        return candies

    # Time O(n) max is O(n), n iterations, in place array modification is O(1)
    # Space O(1) no extra memory used