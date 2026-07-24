class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-2
        ans=-1

        while l<=r:
            mid=(l+r)//2
            if nums[mid]<nums[mid+1]:

                 l=mid+1
            
            else:
                
                ans=mid

                r=mid-1

           
        return ans
        