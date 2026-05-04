class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while(l<=r):
            mid=(l+r)//2
            if(nums[mid]==target):
                return mid
            #Search in left sorted section
            if(nums[l]<=nums[mid]):
                #mid is in left sorted portion
                if(target>nums[mid] or nums[l]>target):
                    l=mid+1
                else:
                    r=mid-1
            else:
                #mid is in right sorted portion
                if(target<nums[mid] or nums[r]<target):
                    r=mid-1
                else:
                    l=mid+1
        return -1
                

                    
                
        