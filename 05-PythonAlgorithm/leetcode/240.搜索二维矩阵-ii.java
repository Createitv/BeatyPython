/*
 * @lc app=leetcode.cn id=240 lang=java
 *
 * [240] 搜索二维矩阵 II
 */

// @lc code=start
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int col = matrix.length - 1;
        int row = 0;
        while (col >= 0 && row < matrix[0].length) {
            if (matrix[col][row] == target) {
                return true;
            } else if (matrix[col][row] > target) {
                col--;
            } else {
                row++;
            }
        }
        return false;
    }
}

// @lc code=end
