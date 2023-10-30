# RSA Factoring Challenge

## Project Description

The RSA Factoring Challenge is a coding project that involves factorizing numbers into a product of two smaller numbers. The goal is to find two factors (`p` and `q`) for a given number `n`, such that `n = p * q`. While the task may seem straightforward, it becomes complex when applied to large numbers, especially in the context of RSA encryption.

## Project Purpose

The primary purpose of this project is to tackle the challenge of factorizing numbers efficiently. Factorizing is the reverse process of multiplying two prime numbers, and it plays a crucial role in the security of cryptographic algorithms like RSA. The ability to factor large numbers can be used to break RSA encryption, making it essential to explore the factorization process.

## Task 0: Factorize All the Things!

### Task Description

In Task 0, we are presented with a list of natural numbers and asked to factorize them into two smaller numbers. The input is provided in a file, with each line containing a single natural number. The script should read this file, factorize the numbers, and print the results in the format `n = p * q`.

### Usage

```shell
factors <file>
```

- `<file>` is a file containing natural numbers to factor, with one number per line.
- The input is assumed to be valid natural numbers greater than 1.
- There will be no empty lines, and no spaces before or after the valid number.
- The output format for each factorization is `n = p * q`.
- The factors `p` and `q` don't have to be prime numbers.

### Example

```shell
4 = 2 * 2
12 = 6 * 2
34 = 17 * 2
128 = 64 * 2
1024 = 512 * 2
4958 = 2479 * 2
1718944270642558716715 = 343788854128511743343 * 5
9 = 3 * 3
99 = 33 * 3
999 = 333 * 3
9999 = 3333 * 3
9797973 = 3265991 * 3
49 = 7 * 7
239809320265259 = 15485783 * 15485773
```

- The script should run within a time limit of 5 seconds.
- The source code should be included in the repository, and we will only run the executable `factors`.

## Additional Task: RSA Factoring Challenge

### Task Description

The RSA Factoring Challenge also includes an advanced task where the goal is to find prime factors `p` and `q` for a given number `n`. Unlike Task 0, in this task, the factors `p` and `q` are always prime numbers.

### Example

```shell
6 = 3 * 2
77 = 11 * 7
239821585064027 = 15486481 * 15485867
2497885147362973 = 49979141 * 49978553
```

## How the Code Works

The code reads the input file, factors the numbers using efficient algorithms, and prints the factorizations. It employs a while loop to continuously factor the numbers until it finds the prime factors `p` and `q`. The output is then formatted as `n = p * q`.

## Usage

To run the script for Task 0, use the following command:

```shell
./factors <file>
```

Replace `<file>` with the name of the input file.

To run the script for the additional RSA Factoring Challenge task, use a similar command, replacing `<file>` with the name of the input file for this task.

## Author

This project is authored by Martin Magonagona.
