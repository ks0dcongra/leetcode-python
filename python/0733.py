class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(i: int, j: int):
            if (0 <= i < m and 0 <= j < n and image[i][j] == oldColor):         
                image[i][j] = newColor
                for r, c in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                    dfs(r, c)
            else:
                return None
        if not any(image) or image[sr][sc] == newColor: return image
        m, n = map(len,(image,image[0]))
        oldColor = image[sr][sc]
        dfs(sr,sc)
        return image