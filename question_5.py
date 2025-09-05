import numpy as np
import matplotlib.pyplot as plt

# Parameters for the normal distribution
mu = 0      # mean
sigma = 1   # standard deviation

# Generate 1000 random numbers from the normal distribution
random_numbers = np.random.normal(mu, sigma, 1000)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(range(1, 1001), random_numbers, alpha=0.5, color='blue')
plt.title('Scatter Plot of 1000 Random Numbers from a Normal Distribution')
plt.xlabel('Index')
plt.ylabel('Random Number Value')
plt.grid(True)
plt.show()