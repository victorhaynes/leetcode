"""
URL: https://leetcode.com/problems/roman-to-integer/description/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

# Optimal
# Time O(n)
# Spae O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        if len(s) == 1:
            return hashmap[s]

        sum = 0
        i = 0
        while i <= len(s) - 1:
            if i != len(s) -1:
                if s[i] == "I" and s[i+1] == "V":
                    sum += 4
                    i += 2
                    continue
                elif s[i] == "I" and s[i+1] == "X":
                    sum += 9
                    i += 2
                    continue
                elif s[i] == "X" and s[i+1] == "L":
                    sum += 40
                    i += 2
                    continue
                elif s[i] == "X" and s[i+1] == "C":
                    sum += 90
                    i += 2
                    continue
                elif s[i] == "C" and s[i+1] == "D":
                    sum += 400
                    i += 2
                    continue
                elif s[i] == "C" and s[i+1] == "M":
                    sum += 900
                    i += 2
                    continue
                else:
                    sum += hashmap[s[i]]
            else:
                sum += hashmap[s[i]]
            i += 1

        return sum
    

# Or more concisely
class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a dictionary for Roman numeral values
        roman_values = {
            "I": 1, "V": 5, "X": 10, 
            "L": 50, "C": 100, "D": 500, "M": 1000
        }

        # Special cases where subtraction is used
        special_cases = {
            "IV": 4, "IX": 9, 
            "XL": 40, "XC": 90, 
            "CD": 400, "CM": 900
        }

        total = 0
        i = 0

        # Iterate through the string
        while i < len(s):
            # Check if the current and next characters form a special case
            if i + 1 < len(s) and s[i:i+2] in special_cases:
                total += special_cases[s[i:i+2]]
                i += 2  # Skip the next character
            else:
                total += roman_values[s[i]]
                i += 1

        return total
