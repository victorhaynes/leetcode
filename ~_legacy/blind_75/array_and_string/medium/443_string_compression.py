from typing import List
"""
URL: https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
"""

# Optimal O(n), O(1) -- modify chars in place using 2 pointers, return the right (write) pointer which is the position + 1 of the last modified chars element
# write is the length of the modified portion
class Solution:
    def compress(self, chars: List[str]) -> int:
        
        num_chars = len(chars)
        if num_chars < 2:
            return num_chars

        read = 0 # Pointer to read through chars/input array
        write = 0 # Pointer to write the compressed characters

        while read < len(chars):
            char = chars[read]
            count = 0

            # count occurences per the specified character 
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        # write is the index (+1) we left on which represents the length of the modified portion of chars
        return write



        
        # # Original solution with O(n) space where I actually built "s"....confusing prompt
        # s = ""

        # if len(chars) == 1:
        #     s = chars[0]
        #     return 1

        # last_written_char = ""
        # prev_char = chars[0]
        # count = 0
        # for i, c in enumerate(chars):
        #     if c == prev_char:
        #         count += 1
        #     if c != prev_char:
        #         s += prev_char
        #         last_written_char = prev_char
        #         if count > 1 and count < 10:
        #             s+= str(count)
        #         if count > 1 and count >= 10:
        #             digits = len(str(count))
        #             for d in range(digits):
        #                 s+= str(count)[d]
        #         count = 1
        #         prev_char = c
        #     if i == len(chars) - 1 and last_written_char != c:
        #         s += c
        #         if count > 1 and count < 10:
        #             s+= str(count)
        #         if count > 1 and count >= 10:
        #             digits = len(str(count))
        #             for d in range(digits):
        #                 s+= str(count)[d]
        

        # for i,char in enumerate(s):
        #     chars[i] = char

        # while len(chars) != len(s):
        #     chars.pop(-1)


        # return len(chars)
            