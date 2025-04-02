class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroes=0
        l=0
        max_lenght=0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes+=1
                while zeroes > k:
                    if nums[l] == 0:
                        zeroes-=1
                    l+=1
            max_lenght = max(max_lenght, r-l+1)
        return max_lenght