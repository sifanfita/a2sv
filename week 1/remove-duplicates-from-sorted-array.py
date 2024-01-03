class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
      left, right = 0, 1 #the two pointers initially at one and zero index
      while right < len(nums):
            if nums[left] == nums[right]:
              nums.remove(nums[left])
            else:
                left+=1
                right+=1

            

   