class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix or not matrix[0]:
            return 0

        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)

            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

            heights.pop()
            return max_area

        cols = len(matrix[0])
        heights = [0] * cols
        max_rect = 0

        for row in matrix:
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            max_rect = max(max_rect, largestRectangleArea(heights))

        return max_rect