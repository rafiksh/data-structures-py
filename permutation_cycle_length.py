def permutation_cycle_length(permutation):
    p_list = permutation[::]
    temp = permutation[::]
    k = 0
    while True:
        for i in range(len(permutation)):
            p_list[i] = temp[permutation[i]]
        k += 1
        temp = p_list[::]
        if p_list == permutation:
            return k


if __name__ == '__main__':
    print(permutation_cycle_length([4, 3, 2, 0, 1]))
