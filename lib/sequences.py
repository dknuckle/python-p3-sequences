#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    f_s = [0, 1]
    
    while len(f_s) < length:
        next_number = f_s[-1] + f_s[-2]
        f_s.append(next_number)
    print(f_s)
    return