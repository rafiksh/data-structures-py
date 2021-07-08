def sieve_of_eratosthenes(n):
    primeArray = [True for i in range(n + 1)]
    primeArray[0] = False
    primeArray[1] = False
    for num in range(n+1):
        if num * num <= n:
            if primeArray[num]:
                for i in range(num * 2, n + 1, num):
                    primeArray[i] = False
    return primeArray


if __name__ == '__main__':
    print(sieve_of_eratosthenes(20))
