# NUMPY 
import numpy as np 
monthly_values = list(monthly_totals.values())
mean_values = np.mean(monthly_values)
median_values = np.median(monthly_values)
std_deviation = np.std(monthly_values)
percentiles = np.percentile(monthly_values, [25,50,75])
max = np.max(monthly_values)
min = np.min(monthly_values)

range_value = max - min
print(range_value)

monthly_stats = {"mean": mean_values, "median": median_values, "std- deviation" : std_deviation, "Percentiles" : percentiles }

print(monthly_stats)