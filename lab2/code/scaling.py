import matplotlib.pyplot as plt

try:
    print("--- Original Point Coordinates ---")
    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))

    print("\n--- Scaling Options ---")
    print("1. Uniform Scaling")
    print("2. Differential / Non-Uniform Scaling")
    print("3. Scaling with respect to an Arbitrary Point")

    choice = int(input("Enter your choice (1, 2 or 3): "))

    # Uniform scaling
    if choice == 1:
        s = float(input("\nEnter scaling factor: "))

        sx = s
        sy = s

        # Scaling about origin
        cx = 0
        cy = 0

    # Non-uniform / differential scaling
    elif choice == 2:
        sx = float(input("\nEnter X scaling factor (Sx): "))
        sy = float(input("Enter Y scaling factor (Sy): "))

        # Scaling about origin
        cx = 0
        cy = 0

    # Scaling about arbitrary point
    elif choice == 3:
        sx = float(input("\nEnter X scaling factor (Sx): "))
        sy = float(input("Enter Y scaling factor (Sy): "))

        print("\n--- Arbitrary Scaling Point ---")
        cx = float(input("Enter X coordinate of scaling point: "))
        cy = float(input("Enter Y coordinate of scaling point: "))

    else:
        print("Invalid choice! Please enter 1, 2 or 3.")
        exit()

except ValueError:
    print("Invalid input! Please enter numbers only.")
    exit()
# ------------------------------------------------
# SCALING FORMULA
# ------------------------------------------------

x_new = cx + (x - cx) * sx
y_new = cy + (y - cy) * sy


# ------------------------------------------------
# PRINT RESULTS
# ------------------------------------------------

print("\n--- Scaling Result ---")

print(f"Original Point: ({x}, {y})")

if choice == 1:
    print("Scaling Type: Uniform Scaling")
    print(f"Scaling Factor: {sx}")

elif choice == 2:
    print("Scaling Type: Differential / Non-Uniform Scaling")
    print(f"X Scaling Factor: {sx}")
    print(f"Y Scaling Factor: {sy}")

elif choice == 3:
    print("Scaling Type: Scaling about Arbitrary Point")
    print(f"X Scaling Factor: {sx}")
    print(f"Y Scaling Factor: {sy}")
    print(f"Scaling Point: ({cx}, {cy})")

print(f"Scaled Point: ({x_new:.2f}, {y_new:.2f})")


# ------------------------------------------------
# PLOT
# ------------------------------------------------

plt.figure(figsize=(7, 7))

# Original point
plt.plot(
    x, y,
    'ro',
    markersize=8,
    label=f'Original ({x}, {y})'
)

# Scaled point
plt.plot(
    x_new, y_new,
    'bo',
    markersize=8,
    label=f'Scaled ({x_new:.2f}, {y_new:.2f})'
)

# Scaling center
plt.plot(
    cx, cy,
    'go',
    markersize=9,
    label=f'Scaling Point ({cx}, {cy})'
)

# Draw line showing scaling
plt.plot(
    [cx, x],
    [cy, y],
    'r--',
    linewidth=1.5
)

plt.plot(
    [cx, x_new],
    [cy, y_new],
    'b--',
    linewidth=1.5
)

# Arrow showing transformation
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


# ------------------------------------------------
# DYNAMIC AXIS LIMITS
# ------------------------------------------------

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


# ------------------------------------------------
# GRID AND AXES
# ------------------------------------------------

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


# ------------------------------------------------
# TITLE
# ------------------------------------------------

if choice == 1:
    plt.title(
        f'2D Uniform Scaling by {sx}'
    )

elif choice == 2:
    plt.title(
        f'2D Non-Uniform Scaling (Sx={sx}, Sy={sy})'
    )

else:
    plt.title(
        f'2D Scaling about ({cx}, {cy})'
    )

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.legend(loc='best')

# Equal X and Y scale
plt.axis('equal')

plt.show()