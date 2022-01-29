import math 
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return nums[0]
        
        elif len(nums) >= 2:
            curr_max= nums[0]
            max_till_now = curr_max
            for num in range (1,len(nums)):
                # curr_max = max(curr_max+nums[num],nums[num])
                if curr_max+nums[num] > nums[num]:
                    curr_max = curr_max+nums[num]
                else:
                    curr_max = nums[num]

                if curr_max > max_till_now:
                    max_till_now = curr_max

            return max_till_now

        
        
