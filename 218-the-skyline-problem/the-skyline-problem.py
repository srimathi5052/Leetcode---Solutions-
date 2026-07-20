class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        
        events = []

        # Create start and end events
        for left, right, height in buildings:
            events.append((left, -height, right))  # Building starts
            events.append((right, 0, 0))           # Building ends

        events.sort()

        result = []
        heap = [(0, float('inf'))]  # (-height, end)

        for x, negHeight, right in events:

            # Remove buildings that have ended
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            # Add new building
            if negHeight != 0:
                heapq.heappush(heap, (negHeight, right))

            currentHeight = -heap[0][0]

            # Skyline changes
            if not result or result[-1][1] != currentHeight:
                result.append([x, currentHeight])

        return result