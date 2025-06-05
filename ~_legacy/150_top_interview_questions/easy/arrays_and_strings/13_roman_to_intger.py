class Solution:
    def romanToInt(self, s: str) -> int:
        
        count = 0
        left = 0
        right = 1

        roman_to_int_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # the right pointer will terminate the loop
        while right < len(s):
            if s[left] == "I" and s[right] == "V":
                count += 4
                left += 2
                right += 2
            elif s[left] == "I" and s[right] == "X":
                count += 9
                left += 2
                right += 2
            elif s[left] == "X" and s[right] == "L":
                count += 40
                left += 2
                right += 2
            elif s[left] == "X" and s[right] == "C":
                count += 90
                left += 2
                right += 2
            elif s[left] == "C" and s[right] == "D":
                count += 400
                left += 2
                right += 2
            elif s[left] == "C" and s[right] == "M":
                count += 900
                left += 2
                right += 2
            else:
                count += roman_to_int_map[s[left]]
                left += 1
                right += 1
            print(count)

        # if the left pointer has more work to do
        if left < len(s):
            count += roman_to_int_map[s[left]]


        return count