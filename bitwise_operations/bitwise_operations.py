x = 2
y = 3

def bitwise_operations_example():
    print(f'x={x}, y={y}')
    print(f'{x<<y} equals to {x*2**y}', r'({x<<y} equals to {x*2**y})')
    print(f'{x&y} is a result of x&y operation. ',
          'Each bit of output is 1 if both bits of operands are 1 at the same position')
    print(f'{x|y} is a result of x|y operation')
    print(f'{x} equals to {-x-1}', r'({~x} equals to {-x-1})')
    print(f'{x^y} equals to 1. Bits of result of x^y are 1 where bit of x doesn\'qt match bit of y.')