class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        candidate = str2
        while len(candidate) > 0:
            if len(str1) % len(candidate) == 0 and len(str2) % len(candidate) == 0:
                factor_one = int(len(str1) / len(candidate))
                factor_two = int(len(str2) / len(candidate))
                if str1 == factor_one * candidate and str2 == factor_two * candidate:
                    return candidate
            candidate = candidate[0:-1]

        return candidate
