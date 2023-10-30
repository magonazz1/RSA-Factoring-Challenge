#!/usr/bin/python3

import sys

def factorize(number):
    factors = []
    for i in range(2, number + 1):
        while number % i == 0:
            factors.append(i)
            number = number // i
    return factors

def main(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            number = int(line)
            factors = factorize(number)
            if len(factors) == 2:
                print(f"{number}={factors[0]}*{factors[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    main(input_file)
