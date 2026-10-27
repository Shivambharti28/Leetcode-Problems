class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1

        for i in range(len(nums)):
            if nums[i] != i:
                k = k & nums[i]
        return max(0,k)
