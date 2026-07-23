class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque

        dq = deque()
        result = []

        for i in range(len(nums)):
            # Remove indices outside the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Record the maximum when the first window is complete
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result