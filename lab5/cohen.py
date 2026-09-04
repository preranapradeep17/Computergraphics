import matplotlib.pyplot as plt

# Region codes
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


# Function to calculate region code
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


# Cohen-Sutherland Line Clipping Algorithm
def cohen_sutherland_clip(x1, y1, x2, y2,
                          xmin, ymin, xmax, ymax):

    code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)

    while True:

        # Both endpoints are inside
        if code1 == 0 and code2 == 0:
            return x1, y1, x2, y2

        # Both endpoints are outside
        elif code1 & code2:
            return None

        else:
            # Select an outside point
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # Find intersection point
            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax

            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin

            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax

            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            # Replace the outside point
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(
                    x1, y1, xmin, ymin, xmax, ymax
                )
            else:
                x2, y2 = x, y
                code2 = compute_code(
                    x2, y2, xmin, ymin, xmax, ymax
                )


# Clipping window
xmin, ymin = 2, 2
xmax, ymax = 8, 8

# Line coordinates
x1, y1 = 0, 5
x2, y2 = 10, 7

# Perform clipping
result = cohen_sutherland_clip(
    x1, y1, x2, y2,
    xmin, ymin, xmax, ymax
)

# Plot original line
plt.plot([x1, x2], [y1, y2],
         linestyle="--",
         label="Original Line")

# Draw clipping window
plt.plot(
    [xmin, xmax, xmax, xmin, xmin],
    [ymin, ymin, ymax, ymax, ymin],
    label="Clipping Window"
)

# Plot clipped line
if result:
    cx1, cy1, cx2, cy2 = result

    plt.plot(
        [cx1, cx2],
        [cy1, cy2],
        linewidth=3,
        label="Clipped Line"
    )

    print("Line accepted")
    print("Clipped coordinates:")
    print(f"({cx1:.2f}, {cy1:.2f})")
    print(f"({cx2:.2f}, {cy2:.2f})")

else:
    print("Line rejected")

plt.title("Cohen-Sutherland Line Clipping Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()
