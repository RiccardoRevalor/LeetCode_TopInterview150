class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ['+', '*', '/', '-']
        for t in tokens:
            if t not in op:
                stack.append(int(t))
            else:
                operand2 = stack.pop(-1)
                operand1 = stack.pop(-1)
                if t == '/':
                    stack.append(int(operand1 / operand2))
                elif t == '*':
                    stack.append(operand1 * operand2)
                elif t == '+':
                    stack.append(operand1 + operand2)
                else:
                    stack.append(operand1 - operand2)
        return stack[-1]

        
