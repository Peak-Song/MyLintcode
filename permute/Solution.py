from typing import List

# https://leetcode-cn.com/problems/permutations/
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
class Solution:
    ret_list = []

    @classmethod
    def swap(cls, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def _permute(self, nums: List[int], k, n):
        if k == n:
            self.ret_list.append(nums.copy())
        else:
            for i in range(k, n, 1):
                self.swap(nums, i, k)
                self._permute(nums, k + 1, n)
                self.swap(nums, i, k)

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ret_list.clear()
        self._permute(nums, 0, len(nums))
        return self.ret_list


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]), flush=True)
