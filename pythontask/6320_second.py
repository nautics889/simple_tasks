import random


def repeating_numbers(n):
    integer_list = [random.randint(0, 10) for _ in range(n)]
    print(f'List: {integer_list}')
    repeating_numbers = []
    integer_list_range = range(len(integer_list))

    for i in integer_list_range:
        for j in integer_list_range:
            if i != j and integer_list[i] == integer_list[j] and integer_list[i] not in repeating_numbers:
                repeating_numbers.append(integer_list[i])

    return repeating_numbers


if __name__ == '__main__':
    n = 7

    print(f'Repeating numbers: {repeating_numbers(n)}')