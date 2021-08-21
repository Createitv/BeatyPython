#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#
"""
思路
标签：二分查找
整体思路：首先数组是一个有序数组的旋转，从这个条件可以看出，数组是有大小规律的，可以使用二分查找利用存在的规律快速找出结果
时间复杂度：O(log(n))
算法流程

初始化下标 left 和 right
每次计算中间下标 mid = (right + left) / 2​，这里的除法是取整运算，不能出现小数
当 numbers[mid] < numbers[right]​ 时，说明最小值在 ​[left, mid]​ 区间中，则令 right = mid，用于下一轮计算
当 numbers[mid] > numbers[right]​ 时，说明最小值在 [mid, right]​ 区间中，则令 left = mid + 1，用于下一轮计算
当 numbers[mid] == numbers[right]​ 时，无法判断最小值在哪个区间之中，此时让 right--，缩小区间范围，在下一轮进行判断
为什么是 right-- 缩小范围，而不是 left++？
因为数组是升序的，所以最小值一定靠近左侧，而不是右侧
比如，当存在 [1,2,2,2,2] 这种情况时，left = 0，right = 4，mid = 2，数值满足 numbers[mid] == numbers[right] 这个条件，如果 left++，则找不到最小值
"""
# @lc code=start


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]
# @lc code=end
