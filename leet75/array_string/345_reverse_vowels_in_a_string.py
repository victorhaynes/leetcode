class Solution:
    def reverseVowels(self, s: str) -> str:
        
        solution = list(s)

        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        
        left = 0
        right = len(s) - 1

        while left < right:
            left_vowel = s[left] if s[left] in vowels else False
            right_vowel = s[right] if s[right] in vowels else False

            if left_vowel and right_vowel:
                solution[left] = right_vowel
                solution[right] = left_vowel
                left += 1
                right -= 1
                continue
            
            if not left_vowel:
                left += 1
            if not right_vowel:
                right -= 1

        return "".join(solution)

    # Time O(n): takes O(n) time to make initial solution, then worst case O(n) iterations with constant time, then O(n) time join operation
    # Space O(n): solution is of size n