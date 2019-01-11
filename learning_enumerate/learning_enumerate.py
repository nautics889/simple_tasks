custom_list = ['First', 'Second', 'Third', 'Fourth', 'Fifth']


def _own_enumerate(collection):
    for index in range(len(collection)):
        yield (index+1, collection[index])


def demonstration_builtin_enumerate():
    print('Iterate custom collection with built-in enumerate:')
    for counter, value in enumerate(custom_list):
        print(f'{counter} — {value}')


def own_implementation():
    print('Iterate custom collection with own implementation of enum-generator:')
    for counter, value in _own_enumerate(custom_list):
        print(f'{counter} — {value}')