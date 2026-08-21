import numpy as np
import matplotlib.pyplot as plt

try:
    print("--- Original Point Coordinates ---")
    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))

    print("\n--- Reflection Options ---")
    print("1. Reflection about X-axis")
    print("2. Reflection about Y-axis")

    choice = int(input("Enter your choice (1 or 2): "))

except ValueError:
    print("Invalid input! Please enter numbers only.")
    exit()

# Original point
point = np.array([
    [x],
    [y],
    [1]
])

# Reflection about X-axis
if choice == 1:

    reflection_matrix = np.array([
        [1,  0, 0],
        [0, -1, 0],
        [0,  0, 1]
    ])

    axis_name = "X-axis"

# Reflection about Y-axis
elif choice == 2:

    reflection_matrix = np.array([
        [-1, 0, 0],
        [0,  1, 0],
        [0,  0, 1]
    ])

    axis_name = "Y-axis"

else:
    print("Invalid choice!")
    exit()

# Apply transformation
result = reflection_matrix @ point

x_new = result[0, 0]
y_new = result[1, 0]

# Print results
print("\n--- Reflection Result ---")

print("\nReflection Matrix:")
print(reflection_matrix)

print(f"\nOriginal Point: ({x}, {y})")
print(f"Reflected Point: ({x_new}, {y_new})")

# Plot
plt.figure(figsize=(7, 7))

plt.plot(
    x, y, 'ro',
    markersize=8,
    label=f'Original ({x}, {y})'
)

plt.plot(
    x_new, y_new, 'bo',
    markersize=8,
    label=f'Reflected ({x_new}, {y_new})'
)

# Line connecting original and reflected points
plt.plot(
    [x, x_new],
    [y, y_new],
    'purple',
    linestyle='--',
    linewidth=1.5
)

# Axes
plt.axhline(
    0,
    color='black',
    linewidth=1.2
)

plt.axvline(
    0,
    color='black',
    linewidth=1.2
)

plt.grid(
    color='gainsboro',
    linestyle='-',
    linewidth=0.7
)

# Dynamic limits
padding = 2

plt.xlim(
    min(x, x_new) - padding,
    max(x, x_new) + padding
)

plt.ylim(
    min(y, y_new) - padding,
    max(y, y_new) + padding
)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title(f"2D Reflection about {axis_name}")

plt.legend()
plt.axis("equal")

plt.show()