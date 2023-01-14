"""
File: pyramid.py
----------------
This program displays a colorful pyramid made up of randomly colored rectangles. The program builds the pyramid one
row at a time, reducing the number of 'bricks' by one after each row is built.
"""
import random
import tkinter


CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

SENTINEL = 0            # Stop condition for main while-loop


def draw_pyramid(canvas):
    """
    starting_width centers the pyramid and serves as the first up_x value
    row variable adjusts height and is incremented by one each time for-loop runs
    adjust variable determines the number of 1/2 brick width adjustments and is incremented as for-loop runs
    """
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    bricks_in_row = BRICKS_IN_BASE
    starting_width = (CANVAS_WIDTH - (BRICK_WIDTH * BRICKS_IN_BASE)) // 2
    row = 1
    adjust = 0

    # each run through the for-loop builds a colored row and then bricks_in_row is reduced by one until it reaches 0
    while bricks_in_row != SENTINEL:
        for i in range(bricks_in_row):
            width_adjust = (adjust * 0.5 * BRICK_WIDTH)
            up_x = starting_width + (i * BRICK_WIDTH) + width_adjust
            up_y = CANVAS_HEIGHT - (row * BRICK_HEIGHT)
            down_x = starting_width + ((i + 1) * BRICK_WIDTH) + width_adjust
            down_y = CANVAS_HEIGHT - ((row - 1) * BRICK_HEIGHT)
            canvas.create_rectangle(up_x, up_y, down_x, down_y, fill=get_random_color())
        bricks_in_row -= 1
        row += 1
        adjust += 1


def get_random_color():
    """
    generates three random values and converts the RGB object to a hexadecimal value using the format operator
    line 56 source: https://stackoverflow.com/questions/3380726/converting-an-rgb-color-tuple-to-a-hexidecimal-string
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return '#%02x%02x%02x' % (r, g, b)


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('pyramid')
    canvas = tkinter.Canvas(top, width=width + 2, height=height + 2)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # This is so (0, 0) works correctly,
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    # Draw blue boundary line at bottom of canvas
    canvas.create_line(0, height, width, height, width=1, fill='blue')

    return canvas


def main():
    """
    This program, when completed, displays a pyramid graphically.
    """
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_pyramid(canvas)
    tkinter.mainloop()


if __name__ == '__main__':
    main()
