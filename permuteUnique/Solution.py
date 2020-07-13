from typing import List


# https://leetcode-cn.com/problems/permutations-ii/
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
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
                # 过滤
                # 如果要交换的双方中间已经存在过交换数，则不应该再执行交换
                if i != k and nums[i] in nums[k:i]:
                    continue
                self.swap(nums, i, k)
                self._permute(nums, k + 1, n)
                self.swap(nums, i, k)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ret_list.clear()
        nums.sort()
        self._permute(nums, 0, len(nums))
        return self.ret_list


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1, 1, 3]), flush=True)
