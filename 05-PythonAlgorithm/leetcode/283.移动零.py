#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        >>> moveZeroes([0,1,0,3,12])
        [1,3,12,0,0]
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)

    def moveZeroesSecond(self, nums):
        """
        双指针:
        初始left、right 指针都指向下标0
        开始移动right指针，当right指针不等于0是，左右指针对应元素互换
        移除元素
        类似题目：27.移除元素
        初始化left = 0，然后开始循环数组，遇到非0的数字，赋值给left，left+=1
        循环left走到len(nums) - 1,将剩余的index都替换成0.
        """
        l = r = 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1  # 每次成功交换左指针右移，替换元素的位置即向右摆
            r += 1

    def moveZeroesTop(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 统计非零数 全部放在左边 然后其他元素直接赋0
        n = len(nums)
        k = 0
        for i in range(n):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for j in range(k, n):
            nums[j] = 0

    def moveZeroesOneLine(self, nums: List[int]) -> None:
        nums[:] = [digit for digit in nums if digit] + \
            [0 for _ in range(nums.count(0))]


# @lc code=end
