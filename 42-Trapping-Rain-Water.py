class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        l = [0]*n
        r = [0]*n
        coll = 0

        l[0] = height[0]
        for i in range(1,n):
            l[i] = max(height[i],l[i-1])

        r[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            r[i] = max(height[i],r[i+1])

        for i in range(n):
            a = min(l[i],r[i])
            coll += a-height[i]
        
        return coll