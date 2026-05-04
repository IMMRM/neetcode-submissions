class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start,end=0,len(heights)-1
        maxArea=0
        while(start<end):
            area=min(heights[start],heights[end])*(end-start)
            maxArea=max(area,maxArea)
            if(heights[start]<=heights[end]):
                start+=1
            else:
                end-=1
        return maxArea
            
        