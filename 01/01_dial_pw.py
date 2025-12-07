from math import floor

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
    print(cmd)
    dial.num_times_hit_zero += dial.get_num_times_hit_zero(cmd)
    dial.turn(cmd)

    # Add one to the ounter if we landed on 0
    if (dial.get_current_number() == 0):
      num_times_landed_on_zero += 1
  
  print(f"Number of times the dial landed on zero: {num_times_landed_on_zero}")
  print(f"Number of times the dial hit zero: {dial.num_times_hit_zero}")

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
  
  if (b < 0):
    b = abs(b) - a
    _resting_num = last_num + 1 - b % (last_num + 1)
    if (_resting_num == last_num + 1):
      _resting_num = 0
    return _resting_num
  else:
    b = abs(b) - (last_num + 1 - a)
    _resting_num = (b % (last_num + 1))
    return _resting_num
        
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
    if (_direction < 0):
      # Reduce the distance since we already recorded the first pass
      _distance -= self.current_num
    else:
      # Reduce the distance so we can start adding from 0
      _distance = _distance - (_dial_numbers - self.current_num)

    _hit_zero += floor(_distance / _dial_numbers)
    
    return _hit_zero

if __name__ == "__main__":
  main()