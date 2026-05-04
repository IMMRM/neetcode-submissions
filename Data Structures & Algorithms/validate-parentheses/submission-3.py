class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets=['(','[','{']
        close_brackets=[')',']','}']
        stack=[]
        top=-1
        for i in s:
            if(i in open_brackets):
                top+=1
                stack.append(i)
            elif(i in close_brackets and top>-1):
                if(i==')' and stack[top]=='('):
                    stack.pop()
                    top-=1
                elif(stack[top]=='{' and i=='}'):
                    stack.pop()
                    top-=1
                elif(stack[top]=='[' and i==']'):
                    stack.pop()
                    top-=1
                else:
                    return False
            else:
                return False
        if(top<0):
            return True
        else:
            return False

        