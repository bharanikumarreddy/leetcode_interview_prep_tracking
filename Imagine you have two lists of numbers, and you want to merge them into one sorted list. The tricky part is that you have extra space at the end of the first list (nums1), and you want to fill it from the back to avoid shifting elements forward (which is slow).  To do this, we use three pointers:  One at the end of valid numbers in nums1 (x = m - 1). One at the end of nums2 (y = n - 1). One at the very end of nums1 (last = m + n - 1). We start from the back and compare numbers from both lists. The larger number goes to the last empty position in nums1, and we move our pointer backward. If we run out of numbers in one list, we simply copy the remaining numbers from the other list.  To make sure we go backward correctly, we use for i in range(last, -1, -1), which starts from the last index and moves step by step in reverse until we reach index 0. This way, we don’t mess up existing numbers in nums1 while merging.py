class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        n=len(nums)

        while i<n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n-=1
            else:
                i=i+1
        return n
        

       # time =o(n)
      '''  nums = [0,1,2,2,3,0,4,2], val = 2
 we can do by two pointer method, I will put a pointer called "i" at 0th index and one pointer at last element of the list 
while i<n ----- 'i' will be incrementing forward (+1) and n will be decrementing backward (-1)
if 0th index element is equal to var then we replace it with last element ,but we only decrement 'n' because we are yet to verify the the new element we  got after 
replacing the 0th index is not 'var'. 
else we incremnet 'i' whne the loop runs gaian and finds out the elenet at i is not eqaul to var we increment 




''''
