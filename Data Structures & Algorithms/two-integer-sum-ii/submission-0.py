class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front,back=0,len(numbers)-1
        while(front!=back):
            sum_val=numbers[front]+numbers[back]
            if(sum_val==target):
                return [front+1,back+1]
            if(sum_val<target):
                front+=1
            else:
                back-=1
        
        