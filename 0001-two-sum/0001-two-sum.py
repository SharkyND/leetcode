class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def checkSum(currentNumber, array):
            for index, element in enumerate(array):
                if element+currentNumber == target:
                    return index
        
        for index, element in enumerate(nums):
            result = checkSum(element,nums[index+1:])            
            if result is not None:
                return [index, result+index+1]

    