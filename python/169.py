class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority, count = None, 0
        for num in nums:
            if count == 0:
                majority = num
            count = count+1 if num == majority else count - 1
        return majority 