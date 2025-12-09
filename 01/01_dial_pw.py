from math import floor
import time

start_time = time.perf_counter()

def main():
  
  # Import test data
  filename = "01/input.aocin"
  
  with open(filename, "r") as file:
    content = file.readlines()
    dial_commands = [f.strip("\n") for f in content]

  # Set up a new dial
  dial = Dial()
  num_times_landed_on_zero = 0
  
  # Turn the dial
  for cmd in dial_commands:
    dial.num_times_hit_zero += dial.get_num_times_hit_zero(cmd)
    dial.turn(cmd)

    # Add one to the ounter if we landed on 0
    if (dial.get_current_number() == 0):
      num_times_landed_on_zero += 1
  
  print(f"Number of times the dial landed on zero: {num_times_landed_on_zero}")
  print(f"Number of times the dial hit zero: {dial.num_times_hit_zero}")
  end_time = time.perf_counter()
  elapsed_time = end_time - start_time
  print(f"Elapsed time: {elapsed_time:.6f} seconds")

def parse_command(command):
  _direction, _distance = command[0], int(command[1:])
  
  if (_direction == "L"):
    _direction = -1
  else:
    _direction = 1
  
  return _direction, _distance

# Clamps sum of two numbers to a range
def get_num_in_range(a, b, first_num, last_num):
  _sum = a + b
  
  # If the 2nd summand is 0
  if (b == 0):
    return _sum
  
  # Check if it doesn't go outside of the number line 
  if (_sum <= last_num and _sum >= first_num):
    return _sum
  
  # Get the remainder of distance to turn (removing full turns)
  _reduced_b = get_reduced_dial_distance(a, b, last_num)
  _remainder = _reduced_b % (last_num + 1)
  
  # Going to the left vs right
  if (b < 0):
    # If the remainder was 0, the remaining distance to turn was either 0 or a multiple of the dial,
    # so we want to end up back at the first number.
    # Otherwise, we want to "turn back" the number of clicks for the remainder
    if (_remainder == 0):
      return first_num
    else:
      return last_num + 1 - _remainder
  else:
    return _remainder

def get_reduced_dial_distance(a, b, last_num):
  if (b < 0):
    b = abs(b) - a
  else:
    b = abs(b) - (last_num + 1 - a)
  
  return b

class Dial:
  def __init__(self, first_num=0, last_num=99, current_num=50):
    self.first_num = first_num
    self.last_num = last_num
    self.current_num = current_num
    self.num_times_hit_zero = 0
  
  # Returns the number it is currently on
  def get_current_number(self):
    return self.current_num
  
  # Turns the dial based on a command in the form of "L#" for left or "R#" for right
  def turn(self, command):
    _direction, _distance = parse_command(command)
    self.current_num = get_num_in_range(self.current_num, _direction * _distance, self.first_num, self.last_num)

  def get_num_times_hit_zero(self, command):
    _direction, _distance = parse_command(command)
    _dial_numbers = self.last_num + 1 - self.first_num
    _new_num = self.current_num + _direction * _distance
    
    _hit_zero = 0
    
    # Check if it doesn't go outside of the number line
    if ((_new_num <= self.last_num and _new_num > self.first_num) or _distance == 0):
      return _hit_zero      
    
    # It passes at least once. Record the first hit and subtract what it took to get there
    if (not (_direction < 0 and self.current_num == 0)):
      _hit_zero += 1
    
    # Check how many more times it passes
    # Reduce the distance since we already recorded the first pass
    _distance = get_reduced_dial_distance(self.current_num, _direction * _distance, self.last_num)

    _hit_zero += floor(_distance / _dial_numbers)
    
    return _hit_zero

if __name__ == "__main__":
  main()