def sum(user_input):
    total=0
    for x in range(int(user_input)):
        total += int(user_input)
    return total


if __name__ == '__main__':
    user_input = input("Enter:")
    print(sum(user_input))
