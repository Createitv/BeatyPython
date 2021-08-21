#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                # 先不存所有值，可得第一个题解
                return [hashtable[target - num], i]
            # 不满足要求再存
            hashtable[nums[i]] = i
        return []


# @lc code=end
