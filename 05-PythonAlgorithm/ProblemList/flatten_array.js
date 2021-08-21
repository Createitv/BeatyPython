// -*- encoding: utf-8 -*-
// FileName    :   flatten_array.js
// Time  : 2021/05/28 17:04:40
// Theme : 拍平数组
// Description : 将多维数组转化为一位数组

/*
// -------------example------------------
flatten([ [ [ [1], 2], 3], [4], [], [[5]]]);
// -> [1, 2, 3, 4, 5]
flatten(['abc', ['def', ['ghi', ['jkl']]]]);
// -> ['abc', 'def', 'ghi', 'jkl']
*/

// O(n)
function flatten(nestedArray) {
	const newArray = [];

	for (let i = 0; i < nestedArray.length; i++) {
		const thisItem = nestedArray[i];

		if (Array.isArray(thisItem)) {
			const flatItem = flatten(thisItem);
			for (let j = 0; j < flatItem.length; j++) {
				newArray.push(flatItem[j]);
			}
		} else {
			newArray.push(thisItem);
		}
	}

	return newArray;
}
console.assert(flatten([[[1], 2], 3, 4, [5]]) === [1, 2, 3, 4, 5], "yes");
console.log(flatten([[[1], 2], 3, 4, [5]]));

// 指定层数拍平
const eachFlat = (arr = [], depth = 1) => {
	const result = []; // 缓存递归结果
	// 开始递归
	(function flat(arr, depth) {
		// forEach 会自动去除数组空位
		arr.forEach((item) => {
			// 控制递归深度
			if (Array.isArray(item) && depth > 0) {
				// 递归数组
				flat(item, depth - 1);
			} else {
				// 缓存元素
				result.push(item);
			}
		});
	})(arr, depth);
	// 返回递归结果
	return result;
};