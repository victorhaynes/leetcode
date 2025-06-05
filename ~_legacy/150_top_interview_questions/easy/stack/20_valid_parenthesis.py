class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "([{":
                stack.append(char) # add open parenthesis to top of stack
            else:
                if not stack:
                    return False # if we have nothig in the stack return False
                opener = stack.pop()
                if char == ")" and opener == "(": # if valid continue, same below
                    continue
                if char == "]" and opener == "[":
                    continue
                if char == "}" and opener == "{":
                    continue

                return False # if invalid scenario go ahead and stop process

        return not stack

# Time: O(n)
# Space: O(n)