import numpy as np
import matplotlib.pyplot as plt

try:
    print("--- Original Point Coordinates ---")
    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))

    print("\n--- Scaling Options ---")
    print("1. Uniform Scaling")
    print("2. Differential / Non-Uniform Scaling")
    print("3. Scaling about Arbitrary Point")

    choice = int(input("Enter your choice (1, 2 or 3): "))

except ValueError:
    print("Invalid input! Please enter numbers only.")
    exit()

# Original point
point = np.array([
    [x],
    [y],
    [1]
])

# ------------------------------------------------
# Uniform Scaling
# ------------------------------------------------

if choice == 1:

    s = float(input("\nEnter scaling factor: "))

    sx = s
    sy = s

    scaling_matrix = np.array([
        [sx, 0,  0],
        [0,  sy, 0],
        [0,  0,  1]
    ])

    center_x = 0
    center_y = 0

    title = f"Uniform Scaling by {s}"

# ------------------------------------------------
# Non-Uniform Scaling
# ------------------------------------------------

elif choice == 2:

    sx = float(input("\nEnter X scaling factor (Sx): "))
    sy = float(input("Enter Y scaling factor (Sy): "))

    scaling_matrix = np.array([
        [sx, 0,  0],
        [0,  sy, 0],
        [0,  0,  1]
    ])

    center_x = 0
    center_y = 0

    title = f"Non-Uniform Scaling (Sx={sx}, Sy={sy})"

# ------------------------------------------------
# Scaling about Arbitrary Point
# ------------------------------------------------

elif choice == 3:

    sx = float(input("\nEnter X scaling factor (Sx): "))
    sy = float(input("Enter Y scaling factor (Sy): "))

    center_x = float(input("Enter X coordinate of scaling point: "))
    center_y = float(input("Enter Y coordinate of scaling point: "))

    # Translate scaling point to origin
    T1 = np.array([
        [1, 0, -center_x],
        [0, 1, -center_y],
        [0, 0, 1]
    ])

    # Scaling matrix
    S = np.array([
        [sx, 0,  0],
        [0,  sy, 0],
        [0,  0,  1]
    ])

    # Translate back
    T2 = np.array([
        [1, 0, center_x],
        [0, 1, center_y],
        [0, 0, 1]
    ])

    # Combined matrix
    scaling_matrix = T2 @ S @ T1

    title = f"Scaling about ({center_x}, {center_y})"

else:
    print("Invalid choice!")
    exit()

# Apply transformation
result = scaling_matrix @ point

x_new = result[0, 0]
y_new = result[1, 0]

# Print results
print("\n--- Scaling Result ---")
print("\nScaling Matrix:")
print(scaling_matrix)

print(f"\nOriginal Point: ({x}, {y})")
print(f"Scaled Point: ({x_new:.2f}, {y_new:.2f})")

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
    label=f'Scaled ({x_new:.2f}, {y_new:.2f})'
)

plt.plot(
    center_x, center_y, 'go',
    markersize=9,
    label=f'Scaling Point ({center_x}, {center_y})'
)

plt.plot(
    [center_x, x],
    [center_y, y],
    'r--'
)

plt.plot(
    [center_x, x_new],
    [center_y, y_new],
    'b--'
)

padding = max(
    abs(x - center_x),
    abs(y - center_y),
    abs(x_new - center_x),
    abs(y_new - center_y),
    2
)

plt.xlim(
    min(x, x_new, center_x) - padding,
    max(x, x_new, center_x) + padding
)

plt.ylim(
    min(y, y_new, center_y) - padding,
    max(y, y_new, center_y) + padding
)

plt.axhline(0, color='black', linewidth=1.2)
plt.axvline(0, color='black', linewidth=1.2)
plt.grid(color='gainsboro', linestyle='-', linewidth=0.7)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title(title)
plt.legend()
plt.axis("equal")

plt.show()