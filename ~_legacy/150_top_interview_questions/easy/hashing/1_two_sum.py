class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,n in enumerate(nums):
            hashmap[n] = i


        for i,n in enumerate(nums):
            compliment = target - n
            if compliment in hashmap and i != hashmap[compliment]: # if the compliment is in the hashmap AND the num we are considering is @ a different index than the compliment:
                return [i, hashmap[compliment]]

        return False

# Time O(n) n iterations twice -> n
# Space O(n) -> n number of dict key/val pairsre