import time

start_time = time.perf_counter()

def main():
  # Import test data
  filename = "03/input.aocin"
  sum_of_max_two_digit_joltage = 0
  sum_of_max_twelve_digit_joltage = 0
  
  with open(filename, "r") as file:
    content = file.readlines()
    battery_banks = [b.strip() for b in content]
  
  for bank in battery_banks:
    joltage = get_max_joltage_n_digits(bank, 2)
    sum_of_max_two_digit_joltage += int(joltage)
    # print(f"Bank: {bank}, Max Joltage: {joltage}")
    
    joltage_n = get_max_joltage_n_digits(bank, 12)
    sum_of_max_twelve_digit_joltage += int(joltage_n)
    # print(f"Bank: {bank}, Max Joltage: {joltage_n}")
    
  print(f"Sum of max joltage: {sum_of_max_two_digit_joltage}")
  print(f"Sum of max 12-digit joltage: {sum_of_max_twelve_digit_joltage}")

def get_max_joltage_n_digits(string_num, n):
  num_length = len(string_num)
  joltage = 0
  
  if (n > num_length or n == 0):
    print("Digits requested exceed string length")
    return 0
  
  if (n == num_length):
    return string_num
  
  if (n < num_length):
    max_digit = 0
    max_digit_pos = 0
    
    for i in range(num_length-n+1):
      num = int(string_num[i])
      if (num > max_digit):
        max_digit = num
        max_digit_pos = i
    
    if (n-1 <= 0):
      return str(max_digit)
    else:
      joltage = str(max_digit) + get_max_joltage_n_digits(string_num[max_digit_pos+1:], n-1)
  
  return joltage

if __name__ == "__main__":
  main()
  
  end_time = time.perf_counter()
  elapsed_time = end_time - start_time
  print(f"Elapsed time: {elapsed_time:.6f} seconds")