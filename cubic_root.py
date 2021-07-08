def cubic_root(n):
    x = 0
    for i in range(0, n + 1):
        if i * i * i <= n:
            x = i
        else:
            break
    sub = n - x * x * x
    text = ", exact!" if sub == 0 else ", not exact with difference " + str(sub)
    print(str(x) + text)


if __name__ == '__main__':
    print(cubic_root(5))
