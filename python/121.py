import operator
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ending_here, max_so_far = 0, 0
        for profit in map(operator.sub, prices[1:], prices):
            max_ending_here = max(max_ending_here + profit, 0)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

# 測試
prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(solution.maxProfit(prices))  # 應輸出5

    
# 如果max_ending_here小於0，就不採用第一天，反之，則繼續採用第一天