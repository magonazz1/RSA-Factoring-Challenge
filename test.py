#!/usr/bin/python3
import sys
import logging

logging.basicConfig(filename='factorization.log', level=logging.INFO, format='%(asctime)s - %(message)s')

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
                result = f"{number}={factors_str}"
                print(result)
                logging.info(result)
    except FileNotFoundError:
        logging.error(f"Error: File '{input_file}' not found.")
        print(f"Error: File '{input_file}' not found.")
    except ValueError:
        logging.error("Error: Input file contains an invalid number.")
        print("Error: Input file contains an invalid number.")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
