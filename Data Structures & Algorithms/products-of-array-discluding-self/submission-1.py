class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero=0
        product=1
        for i in range(0,len(nums)):
            if(nums[i]!=0):
                product*=nums[i]
            else:
                count_zero+=1
        res=[0]*len(nums)
        for j in range(0,len(nums)):
            if(count_zero>1):
                return res
            elif(count_zero==1):
                if(nums[j]==0):
                    res[j]=product
            else:
                res[j]=int(product/nums[j])
        return res

        