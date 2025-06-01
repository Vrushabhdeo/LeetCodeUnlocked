"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.


Constraints:
1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

"""

import math
from collections import deque
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # local_cal = deque()
        #
        # for _ in tokens:
        #     try:
        #         if math.isfinite(int(_)):
        #             print("Appending: " + _)
        #             local_cal.append(int(_))
        #     except:
        #             operand_one = local_cal.pop()
        #             operand_two = local_cal.pop()
        #             print("Popped: {}".format(operand_one))
        #             print("Popped: {}".format(operand_two))
        #
        #             if _ == '+':
        #                 result = operand_two + operand_one
        #             elif _ == '-':
        #                 result = operand_two - operand_one
        #             elif _ == '*':
        #                 result = operand_two * operand_one
        #             elif _ == '/':
        #                 result = int(operand_two / operand_one)
        #
        #             print("Appending result: {}".format(result))
        #             local_cal.append(result)
        #
        # return local_cal[0]
        stack = deque()
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))  # Truncate toward zero

        return stack[0]

solution = Solution()
print(solution.evalRPN(tokens =["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
