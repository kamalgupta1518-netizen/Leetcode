class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=nums1+nums2
        num.sort()
        l=len(num)//2
        if len(num)%2 != 0:
          
            return num[l]
        else:
            k=(num[l]+num[l-1])/2
            return k