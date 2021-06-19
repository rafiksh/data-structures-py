def perfect(number):
    if number <= 0:
        return False
    total = 0
    for x in range(1, number):
        if number % x == 0:
            total += x
    return number == total


if __name__ == '__main__':
    print(perfect(5))
