#!/usr/bin/python3
import sys

def factorize(n):
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factors

def main(input_file):
    try:
        with open(input_file, 'r') as file:
            for line in file:
                number = int(line)
                factors = factorize(number)
                factors_str = ' * '.join(map(str, factors))
                print(f"{number}={factors_str}")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError:
        print("Error: Input file contains an invalid number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
