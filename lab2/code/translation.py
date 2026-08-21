import matplotlib.pyplot as plt

# Get original point coordinates from user input
try:
    print("--- Original Point Coordinates ---")
    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))

    # Get translation shifts from user input
    print("\n--- Translation Vector ---")
    tx = float(input("Enter horizontal shift (tx): "))
    ty = float(input("Enter vertical shift (ty): "))
except ValueError:
    print("Invalid input! Please enter numbers only.")
    exit()

# Calculate new coordinates
x_new = x + tx
y_new = y + ty

# Print results to console
print(f"\nOriginal Point: ({x}, {y})")
print(f"Translated Point: ({x_new}, {y_new})")

# Setup the plot
plt.figure(figsize=(6, 6))

# Plot the points
plt.plot(x, y, 'ro', markersize=8, label=f'Original ({x}, {y})')
plt.plot(x_new, y_new, 'bo', markersize=8, label=f'Translated ({x_new}, {y_new})')

# Draw a directional arrow showing the movement
plt.annotate('', xy=(x_new, y_new), xytext=(x, y),
             arrowprops=dict(arrowstyle="->", color='purple', lw=2, linestyle='--'))

# Dynamic axis limits with padding
padding = max(abs(tx), abs(ty), 2)
plt.xlim(min(x, x_new) - padding, max(x, x_new) + padding)
plt.ylim(min(y, y_new) - padding, max(y, y_new) + padding)

# Grid and origin lines
plt.axhline(0, color='black', linewidth=1.2)
plt.axvline(0, color='black', linewidth=1.2)
plt.grid(color='gainsboro', linestyle='-', linewidth=0.7)

# Labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Interactive 2D Point Translation')
plt.legend(loc='best')

# Show the plot
plt.show()
