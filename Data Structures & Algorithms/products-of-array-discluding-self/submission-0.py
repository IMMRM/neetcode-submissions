class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if(len(nums)<=1):
            return nums
        pref,suff=[0]*len(nums),[0]*len(nums)
        #filling up the prefix
        for i in range(0,len(nums)):
            if(i==0):
                pref[i]=1
            else:
                pref[i]=pref[i-1]*nums[i-1]
        
        #filling up the suffix
        for j in range(len(nums)-1,-1,-1):
            if(j==len(nums)-1):
                suff[j]=1
            else:
                suff[j]=suff[j+1]*nums[j+1]
        #Now starting the calculation
        res=[]
        for i in range(len(nums)):
            res.append(pref[i]*suff[i])
        return res



        
        
        