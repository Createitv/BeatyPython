function selectSort(arr) {
    var len = arr.length;
    var minIndex, temp;
    for (var i = 0; i < len - 1; i++){
        minIndex = i;
        for (var j = i + 1; j < len; j++){
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        [arr[i], arr[minIndex]] =[arr[minIndex], arr[i]]
    }
    return arr
}

var arr2 = selectSort([1, 2, 3, 4, 5, 1, 23]);
console.log(arr2);
    