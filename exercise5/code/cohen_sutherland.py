import matplotlib.pyplot as plt

# --------------------------------------------------
# Region codes
# --------------------------------------------------

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


# --------------------------------------------------
# Find region code of a point
# --------------------------------------------------

def compute_code(x, y, xmin, ymin, xmax, ymax):

    code = INSIDE

    if x < xmin:
        code |= LEFT

    elif x > xmax:
        code |= RIGHT

    if y < ymin:
        code |= BOTTOM

    elif y > ymax:
        code |= TOP

    return code


# --------------------------------------------------
# Cohen-Sutherland Line Clipping
# --------------------------------------------------

def cohen_sutherland(x1, y1, x2, y2,
                     xmin, ymin, xmax, ymax):

    code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)

    accept = False

    while True:

        # Case 1: Both points are inside
        if code1 == 0 and code2 == 0:

            accept = True
            break

        # Case 2: Both points are outside
        # in the same region
        elif (code1 & code2) != 0:

            break

        # Case 3: Line needs clipping
        else:

            # Select the point outside
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # Find intersection point

            # TOP
            if code_out & TOP:

                x = x1 + (x2 - x1) * \
                    (ymax - y1) / (y2 - y1)

                y = ymax

            # BOTTOM
            elif code_out & BOTTOM:

                x = x1 + (x2 - x1) * \
                    (ymin - y1) / (y2 - y1)

                y = ymin

            # RIGHT
            elif code_out & RIGHT:

                y = y1 + (y2 - y1) * \
                    (xmax - x1) / (x2 - x1)

                x = xmax

            # LEFT
            elif code_out & LEFT:

                y = y1 + (y2 - y1) * \
                    (xmin - x1) / (x2 - x1)

                x = xmin

            # Replace the outside point
            if code_out == code1:

                x1 = x
                y1 = y

                code1 = compute_code(
                    x1, y1,
                    xmin, ymin,
                    xmax, ymax
                )

            else:

                x2 = x
                y2 = y

                code2 = compute_code(
                    x2, y2,
                    xmin, ymin,
                    xmax, ymax
                )

    if accept:
        return x1, y1, x2, y2

    else:
        return None


# --------------------------------------------------
# Main Program
# --------------------------------------------------

print("==========================================")
print(" COHEN-SUTHERLAND LINE CLIPPING ALGORITHM")
print("==========================================")

# Clipping window
xmin = float(input("Enter xmin: "))
ymin = float(input("Enter ymin: "))
xmax = float(input("Enter xmax: "))
ymax = float(input("Enter ymax: "))

# Line coordinates
x1 = float(input("\nEnter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))


# Perform clipping
result = cohen_sutherland(
    x1, y1, x2, y2,
    xmin, ymin, xmax, ymax
)


# --------------------------------------------------
# Display result
# --------------------------------------------------

if result is not None:

    x1_clip, y1_clip, x2_clip, y2_clip = result

    print("\nLine is ACCEPTED after clipping.")

    print(
        "Clipped line:",
        f"({x1_clip:.2f}, {y1_clip:.2f})",
        "to",
        f"({x2_clip:.2f}, {y2_clip:.2f})"
    )

else:

    print("\nLine is COMPLETELY OUTSIDE.")
    print("Line is REJECTED.")


# --------------------------------------------------
# Plot
# --------------------------------------------------

plt.figure(figsize=(7, 7))

# Original line
plt.plot(
    [x1, x2],
    [y1, y2],
    'b--',
    label="Original Line"
)

# Clipping window
plt.plot(
    [xmin, xmax, xmax, xmin, xmin],
    [ymin, ymin, ymax, ymax, ymin],
    'k-',
    linewidth=2,
    label="Clipping Window"
)

# Clipped line
if result is not None:

    plt.plot(
        [x1_clip, x2_clip],
        [y1_clip, y2_clip],
        'r-',
        linewidth=3,
        label="Clipped Line"
    )

# Axes
plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Cohen-Sutherland Line Clipping")

plt.grid(True)
plt.legend()
plt.axis("equal")

plt.show()
