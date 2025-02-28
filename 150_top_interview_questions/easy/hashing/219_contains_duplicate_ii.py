class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hashmap = {} # number: index

        for i,n in enumerate(nums):
            if n in hashmap:
                if abs(i - hashmap[n]) <= k:                    
                    return True
            hashmap[n] = i

        return False

    # Time O(n) -> n iterations one pass through nums array
    # Space O(n) -> hashmap of n elements