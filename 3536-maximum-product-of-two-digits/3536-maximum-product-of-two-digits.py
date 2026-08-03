class Solution:
    def maxProduct(self, n: int) -> int:
        n=str(n)
        k=[]
        m=1
        for i in n:
            k.append(int(i))
        k.sort()    
        return k[-1]*k[-2]



