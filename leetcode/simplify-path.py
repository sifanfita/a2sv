class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for char in path.split("/"):
            if char in ('', '.'):
                continue
            elif char in ('..'):
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return '/' + '/'.join(stack)