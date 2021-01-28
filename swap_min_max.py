def swap_min_max(arr: list):
    # Find the maximal element in this list
    max = sorted(arr)[-1]
    # Find the minimal element in this list
    min = sorted(arr, reverse=True)[-1]

    index_max = arr.index(max)
    index_min = arr.index(min)

    # Swap the the position of min and the max
    arr[index_max] = min
    arr[index_min] = max
    print(arr)
