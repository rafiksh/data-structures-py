def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    a = sorted(str1)
    b = sorted(str2)

    for i in range(0, len(str1), 1):
        if str1[i] != str2[i]:
            return False
    return True


if __name__ == '__main__':
    print(is_permutation([2, 0, 1, 4, 3, 5]))
