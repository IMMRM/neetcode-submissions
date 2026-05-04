class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)<2):
            return len(nums)
        hash_set=set(nums)
        max_len=1
        for i in range(0,len(nums)):
            if(nums[i]-1 in hash_set):
                continue
            else:
                begin=nums[i]+1
                ele_len=1
                while(begin in hash_set):
                    ele_len+=1
                    begin+=1
                max_len=max(max_len,ele_len)
        return max_len

        