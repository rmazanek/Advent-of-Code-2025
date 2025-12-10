from math import floor
import time

start_time = time.perf_counter()

def main():
  # Import test data
  filename = "02/input.aocin"
  number_array = []
  sum_of_twice_repeating_ids = 0
  sum_of_any_repeating_ids = 0
  
  with open(filename, "r") as file:
    content = file.readlines()[0].split(",")
    string_array = [s.split("-") for s in content]
    number_array = [[int(s[0]), int(s[1])] for s in string_array]
  
  for endpoints in number_array:
    for n in range(endpoints[0], endpoints[1]+1):
      # Check n for repeating patterns
      if id_digits_repeat_twice(n):
        sum_of_twice_repeating_ids += n
      
      if get_id_digits_repeat_any(n):
        sum_of_any_repeating_ids += n
        
  print(f"Sum of silly twice-repeating ids: {sum_of_twice_repeating_ids}")
  print(f"Sum of any-digits repeating ids : {sum_of_any_repeating_ids}")

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
  string_n = str(n)
  num_digits = len(string_n)
  
  # Skip any 1-digit ids. They cannot repeat
  if (num_digits == 1):
    return False
  
  # Decide on the number of repeating patterns that can be used (1 digit, 2 digits, 3 digits, etc.)
  max_repeat_digits = floor(num_digits / 2)
  
  # First check if all digits are the same. Assume they are until proven wrong
  all_the_same = True
  
  for i in range(num_digits):
    if (string_n[0] != string_n[i]):
      all_the_same = False
      break
  
  if (all_the_same):
    # print(f"{n} is invalid")
    return all_the_same
  
  # Skip a few low primes, which we can't divide up for any remaining checks
  if (num_digits in [2, 3, 5, 7, 11, 13]):
    return False
  
  # Operate down from the highest number (fewer #s to check, fail faster?)
  # We already checked "1 digit" (all the same digit) above
  # Assume the id does not repeat until we find out it does in a test
  id_repeats = False
  
  for digit_test in range(max_repeat_digits, 1, -1):
    # print(f"{n}: {max_repeat_digits}, digit_test:{digit_test}")
    
    # If the digits can't be evenly divided, this digit test cannot pass
    if (num_digits % digit_test != 0):
      # print("Test skipped")
      continue
    
    # For each digit_test, compare the first slice to the next
    # If they do not match at any point, fail this digit test
    digit_test_passes = True
    
    for i in range(0, len(string_n)-digit_test, digit_test):
      first_slice_begin = i
      first_slice_end = first_slice_begin + digit_test
      second_slice_begin = first_slice_end
      second_slice_end = second_slice_begin + digit_test
      
      first_slice = string_n[first_slice_begin:first_slice_end]
      second_slice = string_n[second_slice_begin:second_slice_end]
      # print(f"{first_slice}, {second_slice}")
      
      if (first_slice == second_slice):
        continue
      else:
        digit_test_passes = False
        break
    
    if (digit_test_passes):
      # print(f"{n} is invalid")
      id_repeats = True
      break
    
  return id_repeats

if __name__ == "__main__":
  main()
  
  end_time = time.perf_counter()
  elapsed_time = end_time - start_time
  print(f"Elapsed time: {elapsed_time:.6f} seconds")