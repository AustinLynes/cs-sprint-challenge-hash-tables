def has_negatives(arr):
    """
    YOUR CODE HERE
    """
    arr.sort()

    cache = {}

    # Your code here
    result = []
    cur = arr[0]
    for i in range(len(arr)):
        cache[abs(arr[i])] = 0

    for i in range(len(arr)):
        cache[abs(arr[i])] += 1

    for k, v in cache.items():
        if v > 1:
            result.append(k)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
