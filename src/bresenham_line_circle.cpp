#include <GLUT/glut.h>
#include <cmath>

void drawPixel(int x, int y)
{
    glVertex2i(x, y);
}

// Bresenham Line Algorithm
void bresenhamLine(int x1, int y1, int x2, int y2)
{
    int dx = abs(x2 - x1);
    int dy = abs(y2 - y1);

    int sx = (x1 < x2) ? 1 : -1;
    int sy = (y1 < y2) ? 1 : -1;

    int err = dx - dy;

    glColor3f(1.0, 0.0, 0.0); // Red

    glBegin(GL_POINTS);

    while (true)
    {
        drawPixel(x1, y1);

        if (x1 == x2 && y1 == y2)
            break;

        int e2 = 2 * err;

        if (e2 > -dy)
        {
            err -= dy;
            x1 += sx;
        }

        if (e2 < dx)
        {
            err += dx;
            y1 += sy;
        }
    }

    glEnd();
}

// Plot 8 symmetric points
void plotCircle(int xc, int yc, int x, int y)
{
    glVertex2i(xc + x, yc + y);
    glVertex2i(xc - x, yc + y);
    glVertex2i(xc + x, yc - y);
    glVertex2i(xc - x, yc - y);

    glVertex2i(xc + y, yc + x);
    glVertex2i(xc - y, yc + x);
    glVertex2i(xc + y, yc - x);
    glVertex2i(xc - y, yc - x);
}

// Bresenham Circle Algorithm
void bresenhamCircle(int xc, int yc, int r)
{
    int x = 0;
    int y = r;
    int d = 3 - 2 * r;

    glColor3f(0.0, 1.0, 0.0); // Green

    glBegin(GL_POINTS);

    while (x <= y)
    {
        plotCircle(xc, yc, x, y);

        if (d < 0)
            d = d + 4 * x + 6;
        else
        {
            d = d + 4 * (x - y) + 10;
            y--;
        }

        x++;
    }

    glEnd();
}

void display()
{
    glClear(GL_COLOR_BUFFER_BIT);

    // Draw Line
    bresenhamLine(100, 100, 700, 500);

    // Draw Circle
    bresenhamCircle(400, 300, 150);

    glFlush();
}

void init()
{
    glClearColor(0, 0, 0, 1);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    gluOrtho2D(0, 800, 0, 600);

    glPointSize(3);
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize(800, 600);

    glutCreateWindow("Bresenham Line and Circle");

    init();

    glutDisplayFunc(display);

    glutMainLoop();

    return 0;
}
