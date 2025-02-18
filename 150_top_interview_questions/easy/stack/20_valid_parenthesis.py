"""
URL: https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"\
Output: false

Example 4:
Input: s = "([])"
Output: true


"""
# Optimal
# Time O(n) - n iterations
# Space O(n) - stack of up to size n
# take aways: add open braces to your stack = []
# if it's a closing brace check if the stack has anything it it AND and the last element (First out) is the complement, else return false
class Solution:
    def isValid(self, s: str) -> bool:
        
        open_stack = []
        close_to_open_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char in close_to_open_map: # if it is a closing parenthesis etc.
                if open_stack and open_stack[-1] == close_to_open_map[char]:
                    open_stack.pop()
                else:
                    return False
            else: # if it is an opener
                open_stack.append(char)


        return False if open_stack else True