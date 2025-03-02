class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last=m+n-1
        x=m-1
        y=n-1
        for i in range (last,-1,-1):
            if y<0:
                break
            elif x<0:
                nums1[i]=nums2[y]
                y-=1
            elif nums1[x] < nums2[y]:
                nums1[i]=nums2[y]
                y-=1
            else:
                nums1[i] = nums1[x]
                x-=1




        """
        Do not return anything, modify nums1 in-place instead.
        """
        
