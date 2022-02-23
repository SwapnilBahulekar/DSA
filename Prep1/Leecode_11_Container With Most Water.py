class Solution(object):
    def maxArea(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        
        '''
        i = 0 
        j = i+1 
        traverse till we get if nums[i] > nums[j] - keep incrementing  i,j
        calculate area = (j-i)*nums[j]
        max_area = max(max_area,area)
        increment j till nums[j] > nums[i]
        
        
        '''
        
        i = 0 
        j = len(nums) -1 
        
        area = 0 
        max_area = area
        
        while i < j :
            # print(nums[i],nums[j])
            # print(i,j)
            area=(j - i )* min(nums[i],nums[j])
            print(area)
            max_area= max(max_area,area)
            if nums[i] < nums[j]:
                i+=1
            else:
                j-=1
        
        return max_area
    
            
        
