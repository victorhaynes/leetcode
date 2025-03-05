class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (char == ")" and top != "(") or \
                   (char == "]" and top != "[") or \
                   (char == "}" and top != "{"):
                    return False
        
        return not stack
# Time O(n) - n iterations
# Space O(n) - stack of up to size n
# take aways: add open braces to your stack = []
# if it's a closing brace check if the stack has anything it it AND and the last element (First out) is the complement, else return false
