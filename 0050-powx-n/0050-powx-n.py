class Solution:
    def findpow(self,X,n):
        if n==0:
            return 1
        a= self.findpow(X,n//2)
        if n%2==0:
            return a*a
        else:
            return a*a*X
    def myPow(self, X: float, n: int) -> float:
        if n>=0:
            return self.findpow(X,n)

        else:
            return 1/self.findpow(X,n*(-1))
        