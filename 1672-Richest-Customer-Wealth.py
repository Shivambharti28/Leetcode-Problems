class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        m = len(accounts)
        n = len(accounts[0])
        max_count = 0
        for i in range(m):
            count = 0
            for j in range(n):
                count += accounts[i][j]
            max_count = max(max_count, count)
        return max_count