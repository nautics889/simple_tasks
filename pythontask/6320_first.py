import random


def find_indexes(collection, n):
    indexes = []

    for i in range(len(collection)):
        for j in range(len(custom_collection))[i:]:
            if custom_collection[i] + custom_collection[j] == n and i != j:
                indexes.append((i, j))

    return indexes

if __name__ == '__main__':
    n = 10
    custom_collection = [random.randint(0, 10) for _ in range(random.randint(10, 15))]
    print(f'Collection: {custom_collection}\nIndexes: {find_indexes(custom_collection, n)}')
