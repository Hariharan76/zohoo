import time
def print_number_snake_pattern(n):
    # Initialize the first number
    current_number = 1

    for i in range(1, n + 1):
        if i % 2 == 1:
            # Odd rows: Print numbers in increasing order
            for j in range(current_number, current_number + n):
                time.sleep(2)                
                print(j, end="\t")
            current_number += n
        else:
            # Even rows: Print numbers in decreasing order
            for j in range(current_number + n - 1, current_number - 1, -1):
                time.sleep(5)
                print(j, end="\t")
            current_number += n

        # Move to the next row
        print()

# Example: Print a number snake pattern for n = 4
print_number_snake_pattern(4)
