
# Z-Buffer Algorithm for Hidden Surface Removal

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Screen dimensions
width = 10
height = 10

# Get user input
n = int(input("Enter the number of surfaces: "))

surfaces = []

for i in range(n):
    print(f"\nSurface {i + 1}")

    x1 = int(input("Enter starting x-coordinate (0-9): "))
    y1 = int(input("Enter starting y-coordinate (0-9): "))
    x2 = int(input("Enter ending x-coordinate (1-10): "))
    y2 = int(input("Enter ending y-coordinate (1-10): "))
    z = float(input("Enter depth value (z): "))

    color = input("Enter color (R/G/B): ").strip().upper()

    # Validate input
    if not (0 <= x1 < x2 <= width and
            0 <= y1 < y2 <= height):
        print("Invalid coordinates! Please enter valid ranges.")
        raise SystemExit

    if color not in ['R', 'G', 'B']:
        print("Invalid color! Enter R, G, or B.")
        raise SystemExit

    surfaces.append((x1, y1, x2, y2, z, color))

# Initialize Z-buffer with infinity
z_buffer = np.full((height, width), float('inf'))

# Initialize frame buffer with background
frame_buffer = np.full((height, width), '-', dtype=str)

# Z-buffer algorithm
for x1, y1, x2, y2, z, color in surfaces:

    for y in range(y1, y2):
        for x in range(x1, x2):

            # Smaller depth means closer to viewer
            if z < z_buffer[y, x]:
                z_buffer[y, x] = z
                frame_buffer[y, x] = color

# Display frame buffer
print("\nVisible Surface (Frame Buffer):")

for row in reversed(frame_buffer):
    print(" ".join(row))

# Display Z-buffer
print("\nZ-Buffer (Depth Values):")

for row in reversed(z_buffer):
    print(" ".join(
        f"{value:.1f}" if np.isfinite(value) else "inf"
        for value in row
    ))

# Convert surface colors to RGB for plotting
color_map = {
    '-': [1.0, 1.0, 1.0],  # White
    'R': [1.0, 0.0, 0.0],  # Red
    'G': [0.0, 1.0, 0.0],  # Green
    'B': [0.0, 0.0, 1.0]   # Blue
}

image = np.array([
    [color_map[cell] for cell in row]
    for row in frame_buffer
])

# Plot graphical output
fig, ax = plt.subplots(figsize=(8, 7))

ax.imshow(
    image,
    origin='lower',
    extent=[0, width, 0, height],
    interpolation='nearest'
)

ax.set_title("Z-Buffer Algorithm - Hidden Surface Removal")
ax.set_xlabel("X-coordinate")
ax.set_ylabel("Y-coordinate")

ax.set_xticks(range(width + 1))
ax.set_yticks(range(height + 1))
ax.grid(True, color='gray', alpha=0.5)

legend = [
    Patch(facecolor='red', label='Red Surface'),
    Patch(facecolor='green', label='Green Surface'),
    Patch(facecolor='blue', label='Blue Surface'),
    Patch(facecolor='white', edgecolor='black',
          label='Background')
]

ax.legend(handles=legend)
plt.tight_layout()
plt.show()
