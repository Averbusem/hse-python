"""
https://leetcode.com/problem-list/string/?difficulty=MEDIUM
URL: https://leetcode.com/problems/basic-calculator-ii/?envType=problem-list-v2&envId=string&difficulty=MEDIUM
"""


class Solution(object):
    def get_priority(self, op):
        if op in "+-":
            return 1
        if op in "*/":
            return 2
        return 0

    def apply_operator(self, a, b, op):
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            return a // b

    def to_postfix(self, s):
        output = []
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                digit = 0
                while i < len(s) and s[i].isdigit():
                    digit = digit * 10 + int(s[i])
                    i += 1
                output.append(digit)
                continue  # Пропускаем инкремент i, так как он уже обработан
            elif s[i] in "+-*/":
                while stack and self.get_priority(stack[-1]) >= self.get_priority(s[i]):
                    output.append(stack.pop())
                stack.append(s[i])
            i += 1
        while stack:
            output.append(stack.pop())
        # print(output)
        return output

    def calculate_postfix(self, postfix):
        stack = []
        for elem in postfix:
            if isinstance(elem, str) and elem in "+-*/":
                b = stack.pop()
                a = stack.pop()
                action = self.apply_operator(a, b, elem)
                stack.append(action)
            else:
                stack.append(elem)
        return stack[0]

    def calculate(self, s):
        s = s.replace(" ", "")
        postfix = self.to_postfix(s)
        return self.calculate_postfix(postfix)


sol = Solution()
print(sol.calculate("0-2147483647"))
