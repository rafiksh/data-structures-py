def TwoSum(l, t):
    n = len(l)
    ans = -1
    for i in range(len(l)):
        ans = binarySearch(l, i, n - 1, abs(t - l[i]))
        if ans != -1:
            return True
    return False


def TwoSum(l, t):
    n = len(l)
    first = 0
    last = n - 1
    while first < last:
        if l[first] + l[last] == t:
            return True
        elif l[first] + l[last] > t:
            last -= 1
        else:
            first += 1
    return False


def binarySearch(L, start, end, x):
    if end == start:
        return -1
    if end >= start:
        # nb of elements is end - start
        count = end - start
        mid = start + count // 2
        if L[mid] > x:
            return binarySearch(L, start, mid, x)
        elif L[mid] < x:
            return binarySearch(L, mid + 1, end, x)
        # only other possibility is that element is in middle
        return mid


if __name__ == '__main__':
    print(TwoSum([1, 2, 5, 8], 8))
