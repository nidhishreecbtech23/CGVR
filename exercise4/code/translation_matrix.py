import numpy as np
import matplotlib.pyplot as plt

try:
    print("--- Original Point Coordinates ---")
    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))

    print("\n--- Translation Vector ---")
    tx = float(input("Enter horizontal shift (tx): "))
    ty = float(input("Enter vertical shift (ty): "))

except ValueError:
    print("Invalid input! Please enter numbers only.")
    exit()

# Original point in homogeneous coordinates
point = np.array([
    [x],
    [y],
    [1]
])

# Translation matrix
translation_matrix = np.array([
    [1, 0, tx],
    [0, 1, ty],
    [0, 0, 1]
])

# Apply matrix transformation
result = translation_matrix @ point

x_new = result[0, 0]
y_new = result[1, 0]

# Print results
print("\n--- Translation Result ---")
print("Translation Matrix:")
print(translation_matrix)

print(f"\nOriginal Point: ({x}, {y})")
print(f"Translated Point: ({x_new}, {y_new})")

# Plot
plt.figure(figsize=(6, 6))

plt.plot(
    x, y, 'ro',
    markersize=8,
    label=f'Original ({x}, {y})'
)

plt.plot(
    x_new, y_new, 'bo',
    markersize=8,
    label=f'Translated ({x_new}, {y_new})'
)

plt.annotate(
    '',
    xy=(x_new, y_new),
    xytext=(x, y),
    arrowprops=dict(
        arrowstyle="->",
        color="purple",
        lw=2,
        linestyle="--"
    )
)

padding = max(abs(tx), abs(ty), 2)

plt.xlim(
    min(x, x_new) - padding,
    max(x, x_new) + padding
)

plt.ylim(
    min(y, y_new) - padding,
    max(y, y_new) + padding
)

plt.axhline(0, color='black', linewidth=1.2)
plt.axvline(0, color='black', linewidth=1.2)
plt.grid(color='gainsboro', linestyle='-', linewidth=0.7)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("2D Point Translation using Matrix")
plt.legend()
plt.axis("equal")

plt.show()
