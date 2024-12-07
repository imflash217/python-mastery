def find_sorted_position(_input_array, _target_val):
    """
    Use Binary Search to find the position where _target_val is in _input_array
    or where _target_val should be in _input_array.
    """
    low = 0
    high = len(_input_array) - 1

    while low <= high:
        mid = (low + high) // 2
        if _input_array[mid] == _target_val:
            # value found
            return mid
        elif _target_val < _input_array[mid]:
            # value is present in the left sub-array
            # move the high-pointer to left sub-array
            high = mid - 1
        elif _target_val > _input_array[mid]:
            # value is present in the right sub-array
            # move the low-pointer to right sub-array
            low = mid + 1

    # value not present in the sorted input array
    return low


if __name__ == "__main__":
    input_array = list(map(float, input("give your SORTED array: ").strip().split()))
    target_val = float(input("give your target value: "))
    index = find_sorted_position(input_array, target_val)
    print(f"index: {index}")
