import matplotlib.pyplot as plt
import numpy as np

# Screen size
width, height = 500, 500

# Initialize Z-buffer with infinity
z_buffer = np.full((height, width), float('inf'))

# Initialize image buffer with white color
image = np.ones((height, width, 3))


# Function to draw a triangle
def draw_triangle(vertices, color):
    global z_buffer, image

    x1, y1, z1 = vertices[0]
    x2, y2, z2 = vertices[1]
    x3, y3, z3 = vertices[2]

    # Find bounding box of triangle
    min_x = max(0, int(min(x1, x2, x3)))
    max_x = min(width - 1, int(max(x1, x2, x3)))
    min_y = max(0, int(min(y1, y2, y3)))
    max_y = min(height - 1, int(max(y1, y2, y3)))

    # Check each pixel inside bounding box
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):

            # Calculate barycentric coordinates
            denominator = ((y2 - y3) * (x1 - x3) +
                           (x3 - x2) * (y1 - y3))

            if denominator == 0:
                continue

            a = ((y2 - y3) * (x - x3) +
                 (x3 - x2) * (y - y3)) / denominator

            b = ((y3 - y1) * (x - x3) +
                 (x1 - x3) * (y - y3)) / denominator

            c = 1 - a - b

            # Check whether pixel is inside triangle
            if a >= 0 and b >= 0 and c >= 0:

                # Interpolate depth
                z = a * z1 + b * z2 + c * z3

                # Update Z-buffer if this surface is closer
                if z < z_buffer[y, x]:
                    z_buffer[y, x] = z
                    image[y, x] = color


# Draw two overlapping triangles
draw_triangle(
    [(100, 100, 5), (400, 100, 5), (250, 400, 5)],
    (1, 0, 0)  # Red triangle
)

draw_triangle(
    [(150, 150, 2), (450, 150, 2), (300, 450, 2)],
    (0, 0, 1)  # Blue triangle
)

# Display final image
plt.imshow(image, origin='lower')
plt.title("Z-Buffer Algorithm - Hidden Surface Removal")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()