# https://www.lintcode.com/problem/trapping-rain-water/
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """

    def trapRainWater(self, heights):
        length = len(heights)

        if length < 2:
            return 0

        leftMax = []
        rightMax = []

        # for i in range(length):
        #     if i == 0:
        #         leftMax.append(0)
        #     elif i == 1:
        #         leftMax.append(heights[0])
        #     else:
        #         leftMax.append(max(leftMax[i - 1], heights[i - 1]))

        for i in range(length - 1, -1, -1):
            if i == length - 1:
                rightMax.append(0)
            elif i == length - 2:
                rightMax.append(heights[length - 1])
            else:
                rightMax.append(max(heights[i + 1], rightMax[length - i - 2]))


        # rightMax.reverse()
        # print(rightMax)

        rain = 0
        for i in range(length):
            if i == 0:
                leftMax.append(0)
                rain += 0
                continue
            elif i == 1:
                leftMax.append(heights[0])
            else:
                leftMax.append(max(leftMax[i - 1], heights[i - 1]))

            if leftMax[i] > heights[i] and rightMax[length-i-1] > heights[i]:
                rain += min(leftMax[i], rightMax[length-i-1]) - heights[i]

        # print(leftMax)
        return rain


if __name__ == '__main__':
    print(Solution().trapRainWater([1, 3, 4, 5, 2, 4, 7, 4, 3]))
