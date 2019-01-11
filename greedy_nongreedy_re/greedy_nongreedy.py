import re

def greedy_parsing():
    custom_string = 'Lorem ipsum dolor lorem.'
    template = r'm.+m'

    print(f'Input string: {custom_string}; Template: {template}')

    res = re.search(template, custom_string).group(0)

    print(f'Result: {res}')

def nongreedy_parsing():
    custom_string = 'Lorem ipsum dolor lorem.'
    template = r'm.+?m'

    print(f'Input string: {custom_string}; Template: {template}')

    res = re.search(template, custom_string).group(0)

    print(f'Result: {res}')