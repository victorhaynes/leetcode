# Takeaway: for hashing problems you often want a hashmap of a count or an index

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # "Two-pass" type solution
        # Create a hashmap of values and indicies (1st pass)
        hashmap = {}
        for i,n in enumerate(nums):
            hashmap[n] = i

        # 2nd pass - calculate the compliment, if the complient exists return the current iterator and the index of the compliment
        for i,n in enumerate(nums):
            compliment = target - n

            if compliment in hashmap and i != hashmap[compliment]:
                return [i, hashmap[compliment]]

        return False

# Time: O(n) -> doing n iterations twice which is just n and set membership check which is constant time
# Space O(n) -> hashmap of size n