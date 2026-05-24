class Solution:
    def countBits(self, n: int) -> List[int]:
        def setBits(num):
            count=0
            while(num):
                num=num&(num-1)
                count+=1
            return count
        result=[]
        for i in range(0,n+1):
            result.append(setBits(i))
        return result

        