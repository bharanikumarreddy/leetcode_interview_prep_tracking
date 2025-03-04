class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)  # If array has 2 or fewer elements, return as is
        
        i = 2  # Start from index 2 since the first two elements are always allowed
        for j in range(2, len(nums)):  # Start checking from index 2
            if nums[j] != nums[i - 2]:  # Check if it's allowed (at most two occurrences)
                nums[i] = nums[j]  # Place valid element
                i += 1  # Move insert position forward
        
        return i  
        
