/*
 * @lc app=leetcode.cn id=240 lang=javascript
 *
 * [240] 搜索二维矩阵 II
 */

// @lc code=start
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
	if (!matrix.length) return false;
	let row = matrix.length - 1;
	let col = 0;
	while (col < matrix[0].length && row >= 0) {
		if (matrix[row][col] == target) {
			return true;
		} else if (matrix[row][col] > target) {
			row--;
		} else {
			col++;
		}
	}
	return false;
};

// @lc code=end
