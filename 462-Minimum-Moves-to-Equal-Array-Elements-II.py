class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        median = nums[n//2]
        res = 0
        for i in range(n):
            res += abs(nums[i]-median)
        return res
