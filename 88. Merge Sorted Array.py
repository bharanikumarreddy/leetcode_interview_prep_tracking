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
        
"""
Imagine you have two lists of numbers, and you want to merge them into one sorted list. The tricky part is that you have extra space at the end of the first list (nums1), and you want to fill it from the back to avoid shifting elements forward (which is slow).

To do this, we use three pointers:

One at the end of valid numbers in nums1 (x = m - 1).
One at the end of nums2 (y = n - 1).
One at the very end of nums1 (last = m + n - 1).
We start from the back and compare numbers from both lists. The larger number goes to the last empty position in nums1, and we move our pointer backward. If we run out of numbers in one list, we simply copy the remaining numbers from the other list.

To make sure we go backward correctly, we use for i in range(last, -1, -1), which starts from the last index and moves step by step in reverse until we reach index 0. This way, we don’t mess up existing numbers in nums1 while merging
"""
