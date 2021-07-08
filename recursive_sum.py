def recursive_sum(n):
    total = 0
    for x in range(n+1):
        total += x
    return total


if __name__ == '__main__':
    print(recursive_sum(5))
