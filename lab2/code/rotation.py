import matplotlib.pyplot as plt
import math

try:
    print("--- Original Point Coordinates ---")
    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))

    print("\n--- Rotation Options ---")
    print("1. Rotate about Origin (0, 0)")
    print("2. Rotate about a Given Point")

    choice = int(input("Enter your choice (1 or 2): "))

    # Get rotation angle
    angle = float(input("\nEnter rotation angle (in degrees): "))

    # If rotating about a given point
    if choice == 2:
        print("\n--- Center of Rotation ---")
        cx = float(input("Enter X coordinate of rotation center: "))
        cy = float(input("Enter Y coordinate of rotation center: "))

    elif choice == 1:
        # Center is origin
        cx = 0
        cy = 0

    else:
        print("Invalid choice! Please enter 1 or 2.")
        exit()

except ValueError:
    print("Invalid input! Please enter numbers only.")
    exit()


# Convert angle from degrees to radians
theta = math.radians(angle)

# Rotation formula
x_new = cx + (x - cx) * math.cos(theta) - (y - cy) * math.sin(theta)
y_new = cy + (x - cx) * math.sin(theta) + (y - cy) * math.cos(theta)


# Print results
print("\n--- Rotation Result ---")
print(f"Original Point: ({x}, {y})")

if choice == 1:
    print("Center of Rotation: Origin (0, 0)")
else:
    print(f"Center of Rotation: ({cx}, {cy})")

print(f"Rotation Angle: {angle}°")
print(f"Rotated Point: ({x_new:.2f}, {y_new:.2f})")


# ---------------- PLOT ----------------

plt.figure(figsize=(7, 7))

# Original point
plt.plot(
    x, y, 'ro',
    markersize=8,
    label=f'Original ({x}, {y})'
)

# Rotated point
plt.plot(
    x_new, y_new, 'bo',
    markersize=8,
    label=f'Rotated ({x_new:.2f}, {y_new:.2f})'
)

# Center of rotation
plt.plot(
    cx, cy, 'go',
    markersize=9,
    label=f'Center ({cx}, {cy})'
)

# Line from center to original point
plt.plot(
    [cx, x],
    [cy, y],
    'r--',
    linewidth=1.5
)

# Line from center to rotated point
plt.plot(
    [cx, x_new],
    [cy, y_new],
    'b--',
    linewidth=1.5
)

# Arrow showing movement
plt.annotate(
    '',
    xy=(x_new, y_new),
    xytext=(x, y),
    arrowprops=dict(
        arrowstyle="->",
        color='purple',
        lw=2,
        linestyle='--'
    )
)

# Dynamic axis limits
padding = max(
    abs(x - cx),
    abs(y - cy),
    abs(x_new - cx),
    abs(y_new - cy),
    2
)

plt.xlim(
    min(x, x_new, cx) - padding,
    max(x, x_new, cx) + padding
)

plt.ylim(
    min(y, y_new, cy) - padding,
    max(y, y_new, cy) + padding
)

# Axes and grid
plt.axhline(0, color='black', linewidth=1.2)
plt.axvline(0, color='black', linewidth=1.2)
plt.grid(color='gainsboro', linestyle='-', linewidth=0.7)

# Labels
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

if choice == 1:
    plt.title(f'2D Rotation about Origin by {angle}°')
else:
    plt.title(
        f'2D Rotation about ({cx}, {cy}) by {angle}°'
    )

plt.legend(loc='best')
plt.axis('equal')

plt.show()