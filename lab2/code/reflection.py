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


# ------------------------------------------------
# REFLECTION
# ------------------------------------------------

if choice == 1:
    # Reflection about X-axis
    x_new = x
    y_new = -y

    axis_name = "X-axis"

elif choice == 2:
    # Reflection about Y-axis
    x_new = -x
    y_new = y

    axis_name = "Y-axis"

else:
    print("Invalid choice! Please enter 1 or 2.")
    exit()


# ------------------------------------------------
# PRINT RESULTS
# ------------------------------------------------

print("\n--- Reflection Result ---")

print(f"Original Point: ({x}, {y})")
print(f"Reflection: About {axis_name}")
print(f"Reflected Point: ({x_new}, {y_new})")


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

# Reflected point
plt.plot(
    x_new, y_new,
    'bo',
    markersize=8,
    label=f'Reflected ({x_new}, {y_new})'
)


# Draw line connecting original and reflected points
plt.plot(
    [x, x_new],
    [y, y_new],
    'purple',
    linestyle='--',
    linewidth=1.5
)


# ------------------------------------------------
# AXES
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
# DYNAMIC AXIS LIMITS
# ------------------------------------------------

padding = 2

plt.xlim(
    min(x, x_new) - padding,
    max(x, x_new) + padding
)

plt.ylim(
    min(y, y_new) - padding,
    max(y, y_new) + padding
)


# ------------------------------------------------
# LABELS AND TITLE
# ------------------------------------------------

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title(
    f'2D Reflection about {axis_name}'
)

plt.legend(loc='best')

plt.axis('equal')

plt.show()