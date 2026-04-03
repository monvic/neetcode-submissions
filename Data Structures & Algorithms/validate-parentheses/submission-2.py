class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
                print(stack)
            else:
                if len(stack) == 0:
                    return False
                el = stack.pop() 
                print(el, c)
                if el == '(' and c !=')':
                    return False
                if el == '[' and c !=']':
                    return False
                if el == '{' and c !='}':
                    return False
        if len(stack) != 0:
            return False
        return True
        