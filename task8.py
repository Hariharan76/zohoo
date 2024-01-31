# Partition even and odd numbers in an array

# Iterate through the array and check if each number is even or odd

# Create two separate arrays for even and odd numbers

# Combine the two arrays to get the final partitioned array
def partition_even_odd(arr):
    even_numbers = []
    odd_numbers = []

    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    # Combine the two arrays
    partitioned_array = even_numbers + odd_numbers

    return partitioned_array

# Example usage
input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = partition_even_odd(input_array)

print("Original Array:", input_array)
print("Partitioned Array:", result)
