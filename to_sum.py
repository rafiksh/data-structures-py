def to_sum(user_data):
    total = 0
    for x in range(int(user_data)):
        total += int(user_data)
    return total


if __name__ == '__main__':
    user_input = input("Enter:")
    print(to_sum(user_input))
