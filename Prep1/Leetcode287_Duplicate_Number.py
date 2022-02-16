class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
         [1,3,4,2,2,2]
              i
              j
         
         n = len(s)
         slowpointer 
         fastpointer
         
        '''
        '''
        slowpointer = nums[0]
        fastpointer = nums[0]
        
        
        while True:
            fastpointer = nums[nums[fastpointer]]
            slowpointer = nums[slowpointer]
            if fastpointer == slowpointer:
                break
                
        slowpointer = nums[0]
        while slowpointer!= fastpointer:
            slowpointer = nums[slowpointer]
            fastpointer = nums[fastpointer]
        
        return slowpointer
        '''
        '''
        1,3,4,2,2
        '''
        #binary search solution
        
        
        
        low = 0 
        high = len(nums) - 1
        
        while low <= high:
            curr = (low+high)//2
            count = 0 
            print(curr)
            
            for num in nums:
                if num <= curr:
                    count+=1
            
            # count = sum(num <= cur for num in nums)
            if count > curr:
                duplicate = curr
                high=curr-1
            else:
                low=curr+1
                
        return duplicate
        
        
        
        
