class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        elif n > 1:
            return self.fib(n-1) + self.fib(n-2)
            