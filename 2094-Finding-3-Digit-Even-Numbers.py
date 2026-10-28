class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        set1 = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i!=j and j!=k and i!=k:
                        num = digits[i]*100 + digits[j]*10 + digits[k]
                        if digits[i] != 0 and digits[k]%2 == 0:
                            set1.add(num)
        return sorted(set1)