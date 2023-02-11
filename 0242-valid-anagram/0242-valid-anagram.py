class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s)==sorted(t):
            return True
        return False
        
        # split, sort, join, the function
        
        def splitSortJoin(str):
            splitList = []
            for element in str:
                splitList.append(element)
            
            # sort them
            splitList.sort()

            # join 
            return ''.join(splitList)

        if splitSortJoin(s) == splitSortJoin(t):
            return True
        
        return False