Class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate





from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array
        return nums[len(nums) // 2]  # Return middle element




from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)  # Count occurrences
        for key, val in freq.items():
            if val > len(nums) // 2:
                return key
