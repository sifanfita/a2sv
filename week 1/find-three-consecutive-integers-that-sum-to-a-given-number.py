class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        k=num//3
        m=num%3
        if m != 0:
          print("empty") 
        else:
            return [k-1, k, k+1]

        
        