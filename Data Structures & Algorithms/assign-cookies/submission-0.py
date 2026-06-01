class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        i = j = 0 
        while i < len(g) and j <= len(s):
            if g[i] <= s[i]:
                i += 1
            j += 1
        return i 
        