class Solution(object):
    def maxScore(self, nums, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
        
       
        curr_sum = 0 
        res = 0 
        n= len(nums)
        total_sum = sum(nums)
        start = n - k 
        print(total_sum)
        end =  n 
       
        # print(sum(nums[:1]))
        if k == n:
            return total_sum
        
        else:
           
            curr_sum = sum(nums[:k])
            max_curr_sum = curr_sum
            
            curr_sum = sum(nums[start:end])
            max_curr_sum = max(curr_sum,max_curr_sum)
            for start in range(n-k+1, n):
                end = (start + k - 1) % n
                curr_sum+=nums[end]
                curr_sum-=nums[start - 1]
                max_curr_sum = max(max_curr_sum,curr_sum)
        
        
            return max_curr_sum
        
        
        
        '''
        1,2,3,4,5,6,1
                s   e 
        
        
        '''
        
        
