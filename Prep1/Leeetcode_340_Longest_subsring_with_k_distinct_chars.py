from collections import OrderedDict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        '''
        map = {a:0,}
        dist=1
        res=1
        if element not in hasmap and dist <= k : put in hasmap and increment end
        if element found in hashmap:
           - within window range:
              - if found: distinct count break
              - elif: if duplicate found increment end   
           - outside window range:
              - increment start to end + 1
        else:
            
         k = 2
        'a a a a'  
         s          
               e   
           
         {a:3}
         res=4
        ''' 
        
        if k == 0 and s == None:
            return 0 
        
        else:
            start = 0
            end = 0
            res = 1 
            hashmap = OrderedDict()
            while end < len(s):
                if s[end] in hashmap:
                    del hashmap[s[end]]
                hashmap[s[end]] = end
                end+=1
                print(hashmap)
            
                if len(hashmap) == k + 1:
                    _,del_idx = hashmap.popitem(last = False)
                    print(_,del_idx)
                    start = del_idx + 1
            
                res = max(res, end - start)
                print(res)
            
        return res
