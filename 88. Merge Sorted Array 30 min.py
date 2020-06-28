class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = m - 1
        i2 = n - 1
        iMerged = m + n -1

        while i2 >= 0:
            if i1 < 0 or (nums2[i2] > nums1[i1]):
                nums1[iMerged] = nums2[i2]
                i2 -= 1
            else:
                nums1[iMerged] = nums1[i1]
                i1 -= 1
            
            iMerged -= 1
