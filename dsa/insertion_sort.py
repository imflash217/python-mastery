def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        val = arr[i]
        pos = i
        while pos > 0 and val < arr[pos - 1]:
            # move the array right and decrement the pointer
            arr[pos] = arr[pos - 1]
            pos -= 1
        # swap the value to correct position
        arr[pos] = val

    # return the sorted array
    return arr


if __name__ == "__main__":
    input_arr = list(map(int, input("input the array to be sorted: ").split()))
    sorted_arr = insertion_sort(input_arr)
    print(sorted_arr)
