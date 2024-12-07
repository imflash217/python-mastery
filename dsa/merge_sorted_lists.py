def merge_sorted_lists(list_a, list_b) -> list:
    merged_list = []
    ptr_a = 0
    ptr_b = 0
    while ptr_a < len(list_a) and ptr_b < len(list_b):
        if list_a[ptr_a] < list_b[ptr_b]:
            merged_list.append(list_a[ptr_a])
            ptr_a += 1
        else:
            merged_list.append(list_b[ptr_b])
            ptr_b += 1
    if ptr_a == len(list_a):
        print("ZZZZZ")
        merged_list.extend(list_b[ptr_b:])
    elif ptr_b == len(list_b):
        print("SSSSS")
        merged_list.extend(list_a[ptr_a:])

    return merged_list


if __name__ == "__main__":
    list_a = list(map(float, input("1st sorted list: ").split()))
    list_b = list(map(float, input("2nd sorted list: ").split()))

    merged_list = merge_sorted_lists(list_a, list_b)
    print(merged_list)
