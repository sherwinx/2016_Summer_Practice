class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i == "{" or i == "[" or i == "(":
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif i == "}" and stack.pop() != "{":
                return False
            elif i == "]" and stack.pop() != "[":
                return False
            elif i == ")" and stack.pop() != "(":
                return False
            else:
                continue
        return len(stack) == 0

        """
        :type s: str
        :rtype: bool
        """