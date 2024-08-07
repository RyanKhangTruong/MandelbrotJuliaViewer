import turtle
import mdb_grad

# Creates Turtle Window
turtle.title("Fractal Generator")
turtle.bgcolor('#000000')
turtle.setup(width = 1.0, height = 1.0)
turtle.tracer(0, 0)

# Setting up Turtle
crayon = turtle.Turtle()
crayon.hideturtle()
crayon.penup()
crayon.pensize(1)
crayon.speed(0)

# Generates the Mandelbrot Fractal
def mplot(center, size, cycle):
    crayon.clear()

    for y_coor in range(900):
        crayon.goto(-720, y_coor - 450)
        clr_line = []

        # Calculate the colors of a line
        for x_coor in range(1440):
            comp_num = center + complex(size * (x_coor/720 - 1) * 1.6,
                                        size * (y_coor/450 - 1))
            clr_idx = mdb_grad.mcolor(comp_num, cycle)
            
            if not clr_line:
                clr_line.append([clr_idx, 1])
            elif clr_idx == clr_line[-1][0]:
                clr_line[-1][1] += 1
            else:
                clr_line.append([clr_idx, 1])

        crayon.pendown()

        for clr_seg in clr_line:
            crayon.color(clr_seg[0])
            crayon.forward(clr_seg[1])

        crayon.penup()
        if (y_coor + 1) % 90 == 0:
            turtle.update()

    turtle.update()

# Generates the Julia Fractal
def jplot(center, const, size, cycle):
    crayon.clear()

    for y_coor in range(900):
        crayon.goto(-720, y_coor - 450)
        clr_line = []

        # Calculate the colors of a line
        for x_coor in range(1440):
            comp_num = center + complex(size * (x_coor/720 - 1) * 1.6,
                                        size * (y_coor/450 - 1))
            clr_idx = mdb_grad.jcolor(comp_num, const, cycle)
            
            if not clr_line:
                clr_line.append([clr_idx, 1])
            elif clr_idx == clr_line[-1][0]:
                clr_line[-1][1] += 1
            else:
                clr_line.append([clr_idx, 1])

        crayon.pendown()

        for clr_seg in clr_line:
            crayon.color(clr_seg[0])
            crayon.forward(clr_seg[1])

        crayon.penup()
        if (y_coor + 1) % 90 == 0:
            turtle.update()

    turtle.update()

if __name__ == '__main__':
    # mplot(0+0j, 2, 1)
    jplot(0+0j, -1+0j, 2, 1)
    turtle.done()