import numpy as np
import matplotlib.pyplot as plt
import math

try:
    print("--- Original Point Coordinates ---")
    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))

    print("\n--- Rotation Options ---")
    print("1. Rotation about Origin")
    print("2. Rotation about Given Point")

    choice = int(input("Enter your choice (1 or 2): "))

    angle = float(input("\nEnter rotation angle (in degrees): "))

except ValueError:
    print("Invalid input! Please enter numbers only.")
    exit()

theta = math.radians(angle)

# Original point
point = np.array([
    [x],
    [y],
    [1]
])

# Rotation about origin
if choice == 1:

    rotation_matrix = np.array([
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta),  math.cos(theta), 0],
        [0,               0,               1]
    ])

    center_x = 0
    center_y = 0

    title = f"Rotation about Origin by {angle}°"

# Rotation about arbitrary point
elif choice == 2:

    center_x = float(input("Enter X coordinate of rotation point: "))
    center_y = float(input("Enter Y coordinate of rotation point: "))

    # Translate center to origin
    T1 = np.array([
        [1, 0, -center_x],
        [0, 1, -center_y],
        [0, 0, 1]
    ])

    # Rotation matrix
    R = np.array([
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta),  math.cos(theta), 0],
        [0,               0,               1]
    ])

    # Translate back
    T2 = np.array([
        [1, 0, center_x],
        [0, 1, center_y],
        [0, 0, 1]
    ])

    # Combined transformation
    rotation_matrix = T2 @ R @ T1

    title = f"Rotation about ({center_x}, {center_y}) by {angle}°"

else:
    print("Invalid choice!")
    exit()

# Apply transformation
result = rotation_matrix @ point

x_new = result[0, 0]
y_new = result[1, 0]

# Print results
print("\n--- Rotation Result ---")
print("\nRotation Matrix:")
print(rotation_matrix)

print(f"\nOriginal Point: ({x}, {y})")
print(f"Rotated Point: ({x_new:.2f}, {y_new:.2f})")

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
    label=f'Rotated ({x_new:.2f}, {y_new:.2f})'
)

plt.plot(
    center_x, center_y, 'go',
    markersize=9,
    label=f'Center ({center_x}, {center_y})'
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