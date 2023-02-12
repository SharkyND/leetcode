class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def checkSum(currentNumber, array):
            for indx, elementLocal in enumerate(array):
                if elementLocal+currentNumber == target:
                    return indx
        
        for index, element in enumerate(nums):
            result = checkSum(element,nums[index+1:])            
            if result is not None:
                return [index, result+index+1]

    