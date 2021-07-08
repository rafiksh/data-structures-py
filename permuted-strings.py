def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


def get_permutation_list(input_str, output_str):
    result = []
    for i in range(len(output_str)):
        for j in range(len(input_str)):
            if output_str[i] == input_str[j]:
                if j not in result:
                    result.append(j)
                    break
    return result


if __name__ == '__main__':
    print(is_permutation('sda', 'asd'))
    print(get_permutation_list('ABBC', 'ABCB'))
