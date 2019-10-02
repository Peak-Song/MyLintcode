# https://www.lintcode.com/problem/dices-sum/
class Solution:
    d = {
        (1, 1): 1 / 6,
        (1, 2): 1 / 6,
        (1, 3): 1 / 6,
        (1, 4): 1 / 6,
        (1, 5): 1 / 6,
        (1, 6): 1 / 6
    }

    numbers = [1, 2, 3, 4, 5, 6]

    def p(self, num, sum_):
        if num != 1:
            res = 0
            for i in self.numbers:
                if num - 1 <= sum_ - i <= 6 * (num - 1):
                    if (num - 1, sum_ - i) not in self.d:
                        self.d[(num - 1, sum_ - i)] = self.p(num - 1, sum_ - i)
                    res += self.d[(num - 1, sum_ - i)]

            return res / 6
        else:
            return self.d[(1, sum_)]

    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        array = []
        for i in range(6 * n + 1):
            if i < n:
                continue
            array.append(i)

        # print(array)
        res = []
        # 只计算一半
        half = len(array) / 2
        int_half = int(half)

        if half == int_half:  # 偶数个
            for s in array[:int_half]:
                res.append([s, round(self.p(n, s), 2)])

            for i in range(int_half):
                res.append([array[int_half + i], res[int_half - i -1][1]])
        else:
            for s in array[:int_half]:
                res.append([s, round(self.p(n, s), 2)])

            res.append([array[int_half], round(self.p(n, array[int_half]), 2)])

            for i in range(int_half):
                res.append([array[int_half + 1 + i], res[int_half - i - 1][1]])

        # print(self.d)
        return res


if __name__ == '__main__':
    print(Solution().dicesSum(1))
    # [[2,0.03],[3,0.06],[4,0.08],[5,0.11],[6,0.14],[7,0.17],[8,0.14],[9,0.11],[10,0.08],[11,0.06],[12,0.03]]
    print(Solution().dicesSum(2))
    # [[3,0.00],[4,0.01],[5,0.03],[6,0.05],[7,0.07],[8,0.10],[9,0.12],[10,0.13],[11,0.13],[12,0.12],[13,0.10],
    # [14,0.07],[15,0.05],[16,0.03],[17,0.01],[18,0.00]]
    print(Solution().dicesSum(3))
    # [[4,0.00],[5,0.00],[6,0.01],[7,0.02],[8,0.03],[9,0.04],[10,0.06],[11,0.08],[12,0.10],[13,0.11],[14,0.11],
    # [15,0.11],[16,0.10],[17,0.08],[18,0.06],[19,0.04],[20,0.03],[21,0.02],[22,0.01],[23,0.00],[24,0.00]]
    print(Solution().dicesSum(4))
