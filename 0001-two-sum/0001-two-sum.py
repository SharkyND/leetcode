class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def checkSum(curentIndex):
            for index in range(len(nums)):
                element = nums[index]
                if index == curentIndex:
                    continue
                elif element + nums[curentIndex] == target:
                        return index
            return False
        
        for index in range(len(nums)):
            num = nums[index]
            if checkSum(index)!= False:
                return [index, checkSum(index)]
            