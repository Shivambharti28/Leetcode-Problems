class Solution:
    def minimumCost(self, cost1: int, cost2: int,
                    costBoth: int, need1: int, need2: int) -> int:

        common = min(need1, need2)
        extra = abs(need1 - need2)

        if need1 > need2:
            extraCost = cost1
        else:
            extraCost = cost2

        ans = common * min(costBoth, cost1 + cost2)

        ans += extra * min(costBoth, extraCost)

        return ans