function bubbleSort(arr, even, odd) {
    const n = arr.length;

    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - 1; j++) {
            for (let k = j; k < n; k++) {
                if (arr[j] % 2 === 0 && arr[k] % 2 === 0 && even(arr[j], arr[k]) && arr[j] !== 0 && arr[k] !== 0) {
                    let tmp = arr[j];
                    arr[j] = arr[k];
                    arr[k] = tmp;
                    break
                }
                if (arr[j] % 2 !== 0 && arr[k] % 2 !== 0 && odd(arr[j], arr[k]) && arr[j] !== 0 && arr[k] !== 0) {
                    let tmp = arr[j];
                    arr[j] = arr[k];
                    arr[k] = tmp;
                    break
                }
            }

        }
    }

    return arr;
}

const array = [9, 2, 7, 6, 5, 4, 0, 3, 8, 1];
console.log(bubbleSort(array, (x, y) => {
        return x < y
    }

    , (x, y) => {
        return x > y
    }
));
