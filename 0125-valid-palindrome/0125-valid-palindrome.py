class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.replace(' ','')
        listAlphabat = []
        for element in s:
            if element.isalnum() == True:
                listAlphabat.append(element.lower())
                
        totalLength = len(listAlphabat)
        
        def isSame(listToTest):
            if listToTest == listToTest[::-1]:
                return True
            else:
                return False
        
        return isSame(listAlphabat)
            
            
            