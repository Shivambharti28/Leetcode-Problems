
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = []

        for i in range(n):
            idx = abs(nums[i]) - 1

            if nums[idx] > 0:
                nums[idx] *= -1

        for i in range(n):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans
