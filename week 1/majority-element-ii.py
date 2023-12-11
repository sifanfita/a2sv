class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict_num={}
        ans=[]
        for num in nums:
            if num in dict_num:
                dict_num[num]+=1
            else:
                dict_num[num]=1
        # print(dict_num.keys())
        for key,value in dict_num.items():
            if value>len(nums)/3:
                ans.append(key)
        return ans
        