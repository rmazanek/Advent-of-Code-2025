import time

start_time = time.perf_counter()

def main():
  # Import test data
  filename = "03/input.aocin"
  sum_of_max_joltage = 0
  
  with open(filename, "r") as file:
    content = file.readlines()
    battery_banks = [b.strip() for b in content]
  
  for bank in battery_banks:
    max_digit = 0
    max_digit_pos = 0
    max_second_digit = 0
    
    # Can't be the last digit (we need to make a 2-digit number)
    for i in range(len(bank)-1):
      num = int(bank[i])
      if (num > max_digit):
        max_digit = num
        max_digit_pos = i
  
    # Get the remaining digit
    for i in range(max_digit_pos + 1, len(bank)):
      num = int(bank[i])
      if (num > max_second_digit):
        max_second_digit = num

    joltage = max_digit * 10 + max_second_digit
    sum_of_max_joltage += joltage
    print(f"Bank: {bank}, Max Joltage: {joltage}")
    
  print(f"Sum of max joltage: {sum_of_max_joltage}")

if __name__ == "__main__":
  main()
  
  end_time = time.perf_counter()
  elapsed_time = end_time - start_time
  print(f"Elapsed time: {elapsed_time:.6f} seconds")