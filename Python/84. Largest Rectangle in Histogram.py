class Solution(object):
    def largestRectangleArea(self, heights):
        heights = heights + [0] 
        stack = []  
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = stack.pop()
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                area = heights[h] * width
                if area > max_area:
                    max_area = area
            stack.append(i)

        return max_area
