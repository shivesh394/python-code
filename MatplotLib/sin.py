import math
import matplotlib.pyplot as plt

# Generate x values from 0 to 2*pi with a step of 0.1
x = [i*0.1 for i in range(0, 63)]

# Compute the corresponding y values for sin(x)
y = [math.sin(i) for i in x]

# Plot the sine function
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Function')
plt.show()
