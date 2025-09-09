def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    # Divide (choose pivot)
    pivot = arr[len(arr) // 2]

    # Conquer (partition into 3 lists)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort left and right partitions
    return quick_sort(left) + middle + quick_sort(right)


# Example usage
if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Original Array:", data)
    print("Sorted Array using Quick Sort:", quick_sort(data))
