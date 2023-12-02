class Solution:
    def average(self, salary: List[int]) -> float:
        sum=0
        salary.sort()
        k=len(salary)
        for i in range(1,k-1):
            sum+= salary[i]
        average = sum/(k-2)
        return average
            

        