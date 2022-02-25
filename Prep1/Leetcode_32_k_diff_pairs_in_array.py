class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        
        '''
        
         [3,1,4,1,5]
        
         k = 2 
         [1, 1, 3, 4, 5]
           
                s 
                e
        
        sort array
        if equal move start+=1
        if less move end +=1
        move both start and end forward 
        

        '''
        start = 0 
        end = 1 
        
        nums.sort()
        print(nums)
        res = []
    
        while end < len(nums) and start< len(nums) - 1 :
            diff = nums[end] - nums[start]
            if diff == k:
                if (nums[start],nums[end]) not in res:
                    res.append((nums[start],nums[end]))
                start+=1
                if start == end:
                    end+=1
            elif diff < k:
                end+=1
            else:
                if end == len(nums) - 1:
                    start+=1     
                else:
                    while diff > k :
                        start+=1
                        if start == end:
                            break
                        diff = nums[end] - nums[start]
                        if diff == k:
                            if (nums[start],nums[end]) not in res:
                                res.append((nums[start],nums[end]))
                    end+=1
        return len(res)
            
        
       '''
       Time complexity - O(NLogN)
       Space complexity - O(N)
       
