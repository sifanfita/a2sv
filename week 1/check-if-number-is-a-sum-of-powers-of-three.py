class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
          if n % 3 == 2:
            return False  # If remainder is 2, it's not possible to represent n
          n //= 3  # Divide n by 3
        return True


        