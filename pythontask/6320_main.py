import random


def find_indexes(collection):
    indexes = []

    for i in range(len(collection)):
        for j in range(len(custom_collection)):
            if custom_collection[i]+custom_collection[j] == 10 and i != j:
                if (j, i) not in indexes:
                    indexes.append((i, j))

    return indexes

if __name__ == '__main__':
    custom_collection = [random.randint(0, 10) for _ in range(10)]
    print(f'Collection: {custom_collection}\nIndexes: {find_indexes(custom_collection)}')
