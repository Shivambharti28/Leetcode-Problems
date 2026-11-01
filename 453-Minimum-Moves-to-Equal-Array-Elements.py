class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_value = min(nums)
        total = sum(nums)

        return total - len(nums) * min_value