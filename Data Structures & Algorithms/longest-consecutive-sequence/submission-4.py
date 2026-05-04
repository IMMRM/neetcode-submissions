class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)<2):
            return len(nums)
        nums_set=set(nums)
        max_seq=1
        for i in range(len(nums)):
            if(nums[i]-1 in nums_set):
                continue
            else:
                begin=nums[i]+1
                ele_len=1
                while(begin in nums_set):
                    ele_len+=1
                    begin+=1
                max_seq=max(max_seq,ele_len)
        return max_seq
            

        