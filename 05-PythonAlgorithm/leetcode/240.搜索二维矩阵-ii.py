#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        解题方案
        思路
        标签：数组遍历
        从矩阵的左下角看，上方的数字都比其小，右方的数字都比其大，所以依据该规律去判断数字是否存在
        设当前数字为 cur，目标数字为 target，当 target < cur 时，cur 更新为其上面的数字，当 target > cur 时，cur 更新为其右侧的数字，直到相等则返回 true，否则到了矩阵边界返回 false
        时间复杂度：O(m+n)
        """
        col = 0
        row = len(matrix) - 1
        while (col < len(matrix[0]) and row >= 0):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False
# @lc code=end
