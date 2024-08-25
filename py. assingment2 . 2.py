def even_numbers_tuple(numbers):
 
  even_numbers = []
  for num in numbers:
    if num % 2 == 0:
      even_numbers.append(num)
  return tuple(even_numbers)

# Example usage:
input_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
output_tuple = even_numbers_tuple(input_tuple)
print(output_tuple)
