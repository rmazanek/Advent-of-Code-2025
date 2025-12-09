import time

start_time = time.perf_counter()

with open("01/input.aocin") as f:
    ls = f.read().strip().split("\n")

# Part 1
dial = 50
s = 0
for l in ls:
    d, move = l[0], int(l[1:])
    dial += move if d == "R" else -move
    dial %= 100
    s += dial == 0
print(s)

# Part 2
dial = 50
s = 0
for l in ls:
    d, move = l[0], int(l[1:])
    for _ in range(move):
        dial += 1 if d == "R" else -1
        dial %= 100
        s += dial == 0
print(s)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")