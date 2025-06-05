class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # Two pointers with a lagging pointer "j" (where we want to move NON-val elements to)
        # and a current pointer "i"
            # else:   # you don't actually need to do anything in the else case
            #     nums[i] = "_"


        # Time: O(n)
        # space: O(1)

        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j