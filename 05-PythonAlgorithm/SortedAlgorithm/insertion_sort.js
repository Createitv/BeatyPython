function insertionSort(arr) {
    var len = arr.length
    for (var i = 1; i < len; i++) {
        for (var j = i; j > 0; j--){
            if (arr[j] < arr[j - 1]) {
                [arr[j], arr[j-1]] = [arr[j-1], arr[j]]
            }
        }
    }
    return arr
}

console.log(insertionSort([123,143,543,213,413,13]));