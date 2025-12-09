from math import floor
import time

start_time = time.perf_counter()

def main():
  # Import test data
  filename = "02/input.aocin"
  number_array = []
  sum_of_repeating_ids = 0
  
  with open(filename, "r") as file:
    content = file.readlines()[0].split(",")
    string_array = [s.split("-") for s in content]
    number_array = [[int(s[0]), int(s[1])] for s in string_array]
  
  for endpoints in number_array:
    for n in range(endpoints[0], endpoints[1] + 1):
      # Check n for repeating patterns
      if id_digits_repeat_twice(n):
        sum_of_repeating_ids += n
        
  print(f"Sum of silly ids: {sum_of_repeating_ids}")

def id_digits_repeat_twice(n):
  # See how many digits are in n
  string_n = str(n)
  num_digits = len(string_n)
  
  # Id length must be even to be a fully repeating pair
  if (num_digits % 2 != 0):
    return False
  
  # Decide on the number of digits for repeating pattern (1 digit, 2 digits, 3 digits, etc.)
  max_repeat_digits = floor(num_digits / 2)
  
  # Only check starting from the first digit
  second_slice_begin = max_repeat_digits
  second_slice_end = second_slice_begin + max_repeat_digits
  
  first_slice = string_n[0:max_repeat_digits]
  second_slice = string_n[second_slice_begin:second_slice_end]
  
  return first_slice == second_slice

def get_id_digits_repeat_any(n):
  num_digits = len(str(n))
      
  # Decide on the number of repeating patterns that can be used (1 digit, 2 digits, 3 digits, etc.)
  max_repeat_digits = floor(num_digits / 2)
    # Operate down from the highest number (fewer #s to check, fail faster?)
  
  for digit_test in range(max_repeat_digits, 0, -1):
    print(f"{n}: {max_repeat_digits}, digit_test:{digit_test}")
    string_n = str(n)
    repeated_id = 0
    
    # For each digit of string_n
    for i in range(len(string_n)):
      first_slice_begin = i
      first_slice_end = first_slice_begin + digit_test
      second_slice_begin = first_slice_end
      second_slice_end = second_slice_begin + digit_test
      
      # If the 2nd slice extends past the length of string_n, break
      if (second_slice_end > len(string_n)):
        continue
      
      first_slice = string_n[first_slice_begin:first_slice_end]
      second_slice = string_n[second_slice_begin:second_slice_end]
      print(f"{first_slice}, {second_slice}")
      
      if (first_slice == second_slice):
        #  We've found an id with a repeat, add that number to the ongoing total
        repeated_id = int(string_n)
        print(f"Repeated id is: {repeated_id}")
        break
    
    if (repeated_id != 0):
      return repeated_id

if __name__ == "__main__":
  main()
  
  end_time = time.perf_counter()
  elapsed_time = end_time - start_time
  print(f"Elapsed time: {elapsed_time:.6f} seconds")