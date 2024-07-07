class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        left, right = [], []
        for interval in intervals:
            if interval[1] < start:
                left += [interval]
            elif end < interval[0]:
                right += [interval]
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
        return left + [[start, end]] + right