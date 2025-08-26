import sys
import math
import statistics

numbers = []
count =0
for arg in sys.argv[1:]:
	count += 1
	number = float(arg)
	numbers.append(number)
	
min_val = min(numbers)
max_val = max(numbers)
mean_val = statistics.mean(numbers)
median_val = statistics.median(numbers)

print(count, min_val, max_val, mean_val, median_val) 
