from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        for i in range(len(matrix)):
            heappush(min_heap, [matrix[i][0], i, 0])

        curr_small = 0
        while(min_heap and k > 0):
            curr_small, i, j = heappop(min_heap) 
            k -=1
            if j < len(matrix[0])-1:
                heappush(min_heap, [matrix[i][j+1], i, j+1])

        return curr_small