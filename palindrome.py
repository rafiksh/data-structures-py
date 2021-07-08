def palindrome(input_str):
    return input_str == input_str[::-1]


if __name__ == '__main__':
    print(palindrome('sds'))
