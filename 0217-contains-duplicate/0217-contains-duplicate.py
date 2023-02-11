class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Making sure the number are asecending
        nums.sort()

        for count, element in enumerate(nums):
            previousElement = element
            if count != 0:
                previousElement = nums[count-1]
                if previousElement == element:
                    return True
        return False
        