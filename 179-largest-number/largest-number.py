class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
       
        nums = list(map(str, nums))

        nums.sort(key=lambda x: x * 10, reverse=True)

        result = ''.join(nums)

        return '0' if result[0] == '0' else result