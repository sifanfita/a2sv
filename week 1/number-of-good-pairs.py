class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
       
        k=len(nums)
        l=0
        for i in range(k):
            for j in range(i+1,k):
                if nums[i] != nums[j]:
                    continue
                else:
                    l+=1
        return l


        