import matplotlib.pyplot as plt
import numpy as np

def calculate_fibonacci_levels(low, high):
    diff = high - low
    levels = [0, 0.236, 0.382, 0.618, 1]
    return [high - level * diff for level in levels]

# Stock data
days = list(range(1, 11))
prices = [100, 105, 110, 118, 125, 122, 118, 115, 113, 116]

# Calculate Fibonacci levels
low_price = min(prices)
high_price = max(prices)
fib_levels = calculate_fibonacci_levels(low_price, high_price)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(days, prices, label='TCIN Stock Price')
plt.title('TechInnovate Inc. (TCIN) Stock with Fibonacci Retracement Levels')
plt.xlabel('Days')
plt.ylabel('Price ($)')

# Add Fibonacci levels
colors = ['r', 'g', 'b', 'orange']
labels = ['0%', '23.6%', '38.2%', '61.8%', '100%']
for level, color, label in zip(fib_levels, colors, labels):
    plt.axhline(y=level, color=color, linestyle='--', label=f'{label} ({level:.2f})')

plt.legend()
plt.grid(True)

# Show the plot
plt.show()

# Print Fibonacci levels
print("Fibonacci Retracement Levels:")
for level, label in zip(fib_levels, labels):
    print(f"{label}: ${level:.2f}")
