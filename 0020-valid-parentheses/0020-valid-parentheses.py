class Solution:
    def isValid(self, s: str) -> bool:
        arr = ['2']
        for i in s:
            if i == "(" or i == '{' or  i == '[':
                arr.append(i)
            elif (i == ']' and arr[-1] == '[') or (i == ')' and arr[-1] == '(') or (i == '}' and arr[-1] == '{'):
                arr.pop()
            else:
                return False
        if len(arr) == 1:
            return True
        else:
            return False
