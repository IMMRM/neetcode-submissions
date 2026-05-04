# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root is None):
            return []
        q=deque([root])
        result=[]
        while(q):
            lenQ=len(q)
            level=[]
            for i in range(0,lenQ):
                current_node=q.popleft()
                level.append(current_node.val)
                if(current_node.left):
                    q.append(current_node.left)
                if(current_node.right):
                    q.append(current_node.right)
            result.append(level)
        return result
            

        
        
        
        