import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


# -----------------------------
# Transformation Matrices
# -----------------------------

def translation(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ], dtype=float)


def rotation(angle):
    rad = math.radians(angle)
    c = math.cos(rad)
    s = math.sin(rad)

    return np.array([
        [c, -s, 0],
        [s,  c, 0],
        [0,  0, 1]
    ], dtype=float)


def scaling(sx, sy):
    return np.array([
        [sx, 0,  0],
        [0, sy,  0],
        [0,  0,  1]
    ], dtype=float)


def reflection_x():
    return np.array([
        [1,  0, 0],
        [0, -1, 0],
        [0,  0, 1]
    ], dtype=float)


def reflection_y():
    return np.array([
        [-1, 0, 0],
        [0,  1, 0],
        [0,  0, 1]
    ], dtype=float)


def shearing(shx, shy):
    return np.array([
        [1,   shx, 0],
        [shy, 1,   0],
        [0,   0,   1]
    ], dtype=float)


# -----------------------------
# Original Object
# -----------------------------

triangle = np.array([
    [0, 1, 1],
    [-1, -1, 1],
    [1, -1, 1]
], dtype=float).T


# -----------------------------
# Apply Composite Transformation
# -----------------------------

def composite_transformation():

    # Individual transformations
    T = translation(2, 1)
    R = rotation(30)
    S = scaling(1.5, 1.5)

    # Composite matrix
    # Order: Scale -> Rotate -> Translate
    M = T @ R @ S

    print("Translation Matrix:")
    print(T)

    print("\nRotation Matrix:")
    print(R)

    print("\nScaling Matrix:")
    print(S)

    print("\nComposite Transformation Matrix:")
    print(M)

    # Apply transformation
    transformed_triangle = M @ triangle

    return transformed_triangle


# -----------------------------
# Draw Triangle
# -----------------------------

def draw_triangle(points):

    glBegin(GL_TRIANGLES)

    glVertex2f(points[0][0], points[1][0])
    glVertex2f(points[0][1], points[1][1])
    glVertex2f(points[0][2], points[1][2])

    glEnd()


# -----------------------------
# Display Function
# -----------------------------

def display():

    glClear(GL_COLOR_BUFFER_BIT)

    # Original triangle
    glColor3f(0.0, 0.0, 1.0)

    draw_triangle(triangle)

    # Transformed triangle
    transformed = composite_transformation()

    glColor3f(1.0, 0.0, 0.0)

    draw_triangle(transformed)

    glFlush()


# -----------------------------
# OpenGL Initialization
# -----------------------------

def init():

    glClearColor(1.0, 1.0, 1.0, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(-5, 5, -5, 5)

    glMatrixMode(GL_MODELVIEW)


# -----------------------------
# Main Function
# -----------------------------

def main():

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(100, 100)

    glutCreateWindow(
        b"Experiment 4 - Composite Transformations"
    )

    init()

    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    main()