import argparse
import re


def parse_company_and_username(filename, clear=False):
    try:
        with open(filename, 'r') as input_file:
            for row in input_file:
                if clear:
                    name, company = re.search(r'([\D]+).*@(\w+)', row).groups()
                else:
                    name, company = re.search(r'([\w\.]+)@(\w+)', row).groups()
                yield (name, company)
    except FileNotFoundError:
        print('Input file not found. Please, specify correct file or leave it empty to open "emails.txt" by default')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='emails.txt')
    parser.add_argument('--output', default='output.txt')
    parser.add_argument('-c', '--clear', action='store_true')

    args = parser.parse_args()

    with open(args.output, 'w') as output_file:
        for i in parse_company_and_username(args.input, args.clear):
            output_file.write(f'Company: {i[1]}; Name: {i[0]}\n')
