class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        op = ["+","-","*","/"]
        for c in tokens:
            if c not in op:
                stack.append(c)
            elif c == "+":
                res = int(stack.pop()) + int(stack.pop())
                stack.append(res)
            elif c == "*":
                res = int(stack.pop()) * int(stack.pop())
                stack.append(res)
            elif c == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                if a == 0:
                    return 0
                else:
                    res = int(b/a)
                    stack.append(res)
            elif c == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                res = b-a
                stack.append(res)
            else:
                return 0
        return int(stack[0])


        