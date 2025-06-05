"""
URL: https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
"""

# Optimal - no help
# Time O(n)
# Space O(n)
# strings are close if 1) len are equal 2) unique characters are equal and 3) counts of characters are equal
# (set membership is O(1) operation, unlike an array. true for hash set and hashmap)
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        unique1 = set(word1)
        unique2 = set(word2)

        if unique1 != unique2:
            return False # or do for char in unique1, if not in unique 2 return False. set membership lookup is O(1) same for hashmap/dict


        hash1 = {}
        for char in word1:
            exists = hash1.get(char)
            if exists:
                hash1[char] += 1
            else:
                hash1[char] = 1

        hash2 = {}
        for char in word2:
            exists = hash2.get(char)
            if exists:
                hash2[char] += 1
            else:
                hash2[char] = 1

            
        print(hash1)
        print(hash2)

        values1 = list(hash1.values())
        values2 = list(hash2.values())

        print(values1)
        print(values2)

        counts1 = {}
        for v in values1:
            exists = counts1.get(v)
            if exists:
                counts1[v] += 1
            else:
                counts1[v] = 1

        counts2 = {}
        for v in values2:
            exists = counts2.get(v)
            if exists:
                counts2[v] += 1
            else:
                counts2[v] = 1

        print(counts1)
        print(counts2)

        for count in counts1:
            try:
                if counts1[count] != counts2[count]:
                    return False
            except KeyError:
                return False

        return True