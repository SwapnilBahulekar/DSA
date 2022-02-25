class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        
        '''
         curr = 0 
         start = 0 
         end = len(nums) - 1
        
         [2,0,1]
         
          s    e 
          c
           
         
         compare start and end 
         if less swap start and end
         compare 
         
        '''
        
        curr = 0 
        start = 0 
        end = len(nums) - 1
        
        while curr <= end:
            if nums[curr] == 0:
                nums[curr],nums[start]= nums[start],nums[curr]
                start+=1
                curr+=1
            
            elif nums[curr] == 2:
                nums[curr],nums[end]= nums[end],nums[curr]
                end-=1
            
            else:
                curr+=1
        return nums
      
      
      '''
      Time complexity O(N)
      Space Complexity - O(1)
      '''
        
        
        
        
        
