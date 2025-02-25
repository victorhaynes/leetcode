class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        solution = []

        i = 0
        for chars_tuple in zip(*strs):
            if len(set(chars_tuple)) == 1:
                solution.append(chars_tuple[0])
            else:
                break # only go until there is a missmatch, just stop then


        return "".join(solution)

# Time -> n iterations where n is the longest element in strs, in each iteration we do m work (set conversion, converting the tuple to a set takes the length [m] of the set time)
# Space O(m) -> m space where the m is the length of the longest prefix or potentially the longest word, the set is not held in memory
