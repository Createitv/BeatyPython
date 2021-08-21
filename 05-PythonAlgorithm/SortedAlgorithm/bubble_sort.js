function bubbleSort(arr) {
	var len = arr.length;
	for (var i = 0; i < len - 1; i++) {
		for (var j = 0; j < len - 1 - i; j++) {
			if (arr[j] > arr[j + 1]) {
				[arr[j + 1], arr[j]] = [arr[j], arr[j + 1]];
				// var temp dp;
			}
		}
	}
	return arr;
}
var arr2 = bubbleSort([1, 2, 3, 4, 5, 1, 23]);
console.log(arr2);
