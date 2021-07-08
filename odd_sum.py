def odd_sum(n):
    total = 0
    for x in range(n+1):
        total += x if x % 2 == 1 else 0
        print(total)
    return total


if __name__ == '__main__':
    print(odd_sum(31))
