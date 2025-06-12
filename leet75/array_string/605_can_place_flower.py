class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        c = 0 # center, left, right
        l = c - 1
        r = c + 1
        while n > 0 and c < len(flowerbed):
            if flowerbed[c] == 1:
                pass
            else:            
                try:
                    if l < 0: # out of the left bounds
                        left_open = True
                    else:
                        left_open = False if flowerbed[l] == 1 else True
                except IndexError:
                    left_open = True
                try:
                    right_open = False if flowerbed[r] == 1 else True
                except IndexError:
                    right_open = True

                if left_open and right_open:
                    flowerbed[c] = 1
                    n -= 1
            
            c += 1
            l += 1
            r += 1
        return not n # if n == 0 -> True, if n != 0 -> False
# Time O(n), one pass
# Space O(1) only in place modifications and fixed pointers