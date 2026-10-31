class Solution:
    def maxSumOfSquares(self, num: int, summ: int) -> str:
        if summ > 9*num:
            return ""

        ans = ""
        count_nine = summ // 9

        for i in range(count_nine):
            ans += '9'

        remainder = summ % 9
        if remainder > 0:
            ans += str(remainder)
        zeroes = num - len(ans)

        for i in range(zeroes):
            ans += '0'
        
        return ans