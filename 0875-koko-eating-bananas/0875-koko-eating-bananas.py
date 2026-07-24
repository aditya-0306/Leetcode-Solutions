class Solution:
    def gethours(self,piles,mid):
        ans=0
        for piles in piles:
            ans+=(piles+mid-1)//mid
        return ans
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        k=r
        while l<=r:
            mid=(l+r)//2
            if self.gethours(piles,mid)>h:
                l= mid+1
            else:
                k=mid
                r=mid-1

        return k 

        