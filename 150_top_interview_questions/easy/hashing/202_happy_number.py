class Solution:
    def isHappy(self, n: int) -> bool:
        seen_numbers = set()
        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)

            digits = []
            for d in str(n):
                digits.append(int(d))

            n = 0
            for d in digits:
                n += d**2

        return n == 1

# Time O(logn) -> where d is the number of digits in n, worst case for large numbers it is O(logn)
# Space O(logn) -> Space complexity of the list made in each iteration



        # # Recursive
        # def add_digit_squares(num, seen):
        #     if num == 1:
        #         return True

        #     if num in seen:
        #         return False

        #     seen.add(num)

        #     digits = []
        #     for d in str(num):
        #         digits.append(int(d))

        #     new_number = 0
        #     for d in digits:
        #         new_number += d**2
            
        #     return add_digit_squares(new_number, seen)

        # return add_digit_squares(n, set())



