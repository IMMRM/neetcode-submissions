class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        def findWord(r,c,index):
            # Acceptance condition
            if(index==len(word)):
                return True
            if(r<0 or c<0 or r>=rows or c>=cols or board[r][c]!=word[index]):
                return False
            # Mark the visited node
            temp=board[r][c]
            board[r][c]="#"
            found=(findWord(r-1,c,index+1) or 
                    findWord(r+1,c,index+1) or 
                    findWord(r,c-1,index+1) or 
                    findWord(r,c+1,index+1))
            board[r][c]=temp
            return found

        for i in range(rows):
            for j in range(cols):
                if(findWord(i,j,0)):
                    return True
            
        return False
        
        