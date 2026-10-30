class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = len(heights) - 1
        i = 0
        most = 0
        while i < j:
            length = j - i
            m = min(heights[i], heights[j])
            capacity = length * m
            if capacity > most:
                most = capacity
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return most
        
            
        