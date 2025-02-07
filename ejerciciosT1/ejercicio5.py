

from math import sqrt


def esPrimo (num: int) -> bool:
    i = 1
    while i < sqrt(num):
        if num % i == 0:
            return False
        
