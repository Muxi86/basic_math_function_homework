from math import trunc

def main(a, b):
    '''Find the remainder when a is divided by b and return it.
    
    Args:
        a (int): a number
        b (int): a number
        
    Returns:
        int: the result.
    '''
    return (a % b)

a = int(input())
b = int(input())

print(main(a, b))