# Note: uses "Boyer-Moore Voting Algorithm"
# Time O(n) -> n iterations
# Space O(1) -> no extra memory

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        potential_majority = None
        count = 0

        for n in nums:
            if count == 0:
                potential_majority = n
            
            if n == potential_majority:
                count += 1
            else:
                count -=1

        return potential_majority


        # Easy solution ushing hashing
        # Time O(n) -> one iteration through n
        # Space O(n) -> hash of n size

        # hashmap = {}
        # majority = float('-inf')
        
        # for num in nums:
        #     if hashmap.get(num, False) == False:
        #         hashmap[num] = 1
        #     else:
        #         hashmap[num] = hashmap[num] + 1
            
        #     if hashmap[num] > len(nums)/ 2:
        #         majority = num
        
        # return majority