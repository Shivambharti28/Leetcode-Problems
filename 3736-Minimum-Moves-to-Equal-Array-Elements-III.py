class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)
        res = 0
        for i in range(len(nums)):
            res += abs(nums[i]-maximum)
        return res