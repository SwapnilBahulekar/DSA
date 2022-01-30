class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        'abcabcbb'
        
        
        'pwwkew'
        'dvdf'
        
        '''
        {d:1,v:2}
         
         res= 2
         
        '''
    
        if len(s) == None:
            return "ValueError"
        
        if len(s) == 1:
            return 1
            
        else:
            start=0
            end=0
            res= 0
            hashmap = {}

            for end in range(len(s)):
                if s[end] not in hashmap:
                    res = max(res, end-start+1) #element not in window - increment end pointer and calculate length 
                    
                elif s[end] in hashmap:
                    if hashmap[s[end]] < start: # if element within range increment 
                        res = max(res,end-start+1)
                    else:
                        start = hashmap[s[end]] + 1 # if element found outside range change start to hashmap[s[end]] + 1
                hashmap[s[end]] = end              #keep updating end pointer element in hashmap with value as index "abcabcbb" {u'a': 3, u'c': 5, u'b': 7}

              
            return res
    
            
            
            
            
                
        
        
        
         
        
