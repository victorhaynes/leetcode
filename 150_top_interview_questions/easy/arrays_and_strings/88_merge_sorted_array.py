# Time: O(m+n)
# space: O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Three pointers problem
        # 1) the index where the operation needs to occur
        # 2) and 3) m,n or the indexes of the two arrays our logic needs to consider
        # Remember i and j and last INDEXES

        last = m + n - 1
        i = m - 1
        j = n - 1

        # merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else: # equal or if nums2 is greater
                nums1[last] = nums2[j]
                j -= 1
            last -= 1

        # handle leftovers of nums2
        while j >= 0:
            nums1[last] = nums2[j]
            last -= 1
            j -= 1 


 