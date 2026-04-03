class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = []
        tokens.reverse()
        while tokens:
            c = tokens.pop()
            if c == '+':
                op1 = op.pop()
                op2 = op.pop()
                op.append(op2+op1)
            elif c == '-':
                op1 = op.pop()
                op2 = op.pop()
                op.append(op2-op1)

            elif c=='*':

                op1 = op.pop()
                op2 = op.pop()
                op.append(op2*op1)

            elif c == '/':

                op1 = op.pop()
                op2 = op.pop()
                op.append(int(op2/op1))

            else:
                op.append(int(c))


        return op.pop()
        

        