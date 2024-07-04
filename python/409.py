class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        map = {}
        odd_count = 0
        for i in s:
            map[i] = map.get(i,0) + 1
        for j in map.values():
            if j % 2 == 0:
                ans += j
            else:
                ans += j -1
                odd_count += 1
        if odd_count > 0:
            ans += 1
        return ans
     