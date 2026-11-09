import matplotlib.pyplot as plt
import numpy as np

math = np.array([85, 70, 90, 60, 75, 95, 55, 80, 65, 88])

science = np.array([80, 75, 95, 65, 70, 90, 60, 85, 70, 92])

plt.scatter(math, science, color="blue", marker="o", s=80)

plt.xlabel("Mathematics Marks")
plt.ylabel("Science Marks")
plt.title("Mathematics vs Science Marks of 10 Students")

plt.grid(True)
plt.show()