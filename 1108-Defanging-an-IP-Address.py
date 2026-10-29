class Solution:
    def defangIPaddr(self, address: str) -> str:
        n = len(address)
        r = 0
        res = ""
        while r < n:
            if address[r] == '.':
                res+='[.]'
            else:
                res+=address[r]
            r+=1
        return res