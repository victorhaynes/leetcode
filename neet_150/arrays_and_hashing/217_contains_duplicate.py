class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        hashset = set()
        for n in nums:
            hashset.add(n)

        return True if len(hashset) != len(nums) else False

# Time O(n) -> n loop iterations
# Space O(n) -> set of up to size n