import random


def search_repeating_numbers(n):
    integer_list = [random.randint(0, 10) for _ in range(n)]
    print(f'List: {integer_list}')

    for item in integer_list:
        if integer_list.count(item) >= 2:
            yield item

if __name__ == '__main__':
    n = 7

    repeating_numbers = set()
    for item in search_repeating_numbers(n):
        repeating_numbers.add(item)

    print(f'Repeating numbers: {repeating_numbers}')