#to find the divisors of a number and to add all the divisors to check whether it is greater than the given number

def sum_of_divisors(n):
    divisors = [1]  # Start with 1 as all numbers are divisible by 1
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

def check_divisor_sum(n):
    divisor_sum = sum_of_divisors(n)
    return divisor_sum > n

# Example usage
given_number = 12
result = check_divisor_sum(given_number)

if result:
    print(f"The sum of divisors of {given_number} is greater than {given_number}.")
else:
    print(f"The sum of divisors of {given_number} is not greater than {given_number}.")
