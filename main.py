#do input on how many times to try for the approximate value of pi
iterations = int(input("Please enter how many iterations the program will go through: "))
total = 0
for iteration in range(1, iteratios):
  total += ((-1) ** (iteration + 1))*((1.0 / (iteration+iteration + 1)))

value = 4 * (1 - total)
print(value)