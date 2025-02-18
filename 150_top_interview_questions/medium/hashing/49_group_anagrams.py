# Time: O(n*mlogm)
# Space: O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_strs = {}
        i = 0
        for word in strs:
            if not sorted_strs.get("".join(sorted(word))) and sorted_strs.get("".join(sorted(word))) != 0:
                sorted_strs["".join(sorted(word))] = i
                i += 1

        
        solution = [[]] * i
        for word in strs:
            sorted_word = "".join(sorted(word))
            index_to_update = sorted_strs[sorted_word]

            print(index_to_update, solution)

            if solution[index_to_update] == []:
                solution[index_to_update] = [word]
            else:
                prev = solution[index_to_update]
                ans = prev + [word]
                solution[index_to_update] = ans           


        return solution

    