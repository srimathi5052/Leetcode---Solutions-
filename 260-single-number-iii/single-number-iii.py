class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    
        xor = 0

        # XOR of all numbers
        for num in nums:
            xor ^= num

        # Rightmost set bit
        diff = xor & -xor

        a = 0
        b = 0

        # Divide numbers into two groups
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num

        return [a, b]