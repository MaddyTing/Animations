#Uses lines and circles to create a unique effect!

import simplegui
import random

x = 5
y = 5
xa = 600
ya = 600

def draw_handler(canvas):
    global x
    global y
    x = x + 5
    y = y + 5
    canvas.draw_line((x, y), (0, 0), 10, "Indigo")
    canvas.draw_line((x, y + 500), (0, 0), 10, "#77298E")
    canvas.draw_line((x + 500, y), (0, 0), 10, "Purple")

    canvas.draw_circle((x, 300), 50, 1, "Orange", "Orange")

            
    canvas.draw_circle((300, y), 50, 1, "Red", "Red")
    if(y >= 600):
        global ya
        ya = ya - 5
        canvas.draw_line((0, 0), (600, 600), 10, "Blue")
        canvas.draw_line((ya, ya), (0, 0), 11, "Black")
        canvas.draw_line((x, y + 500), (0, 0), 11, "Black")
        canvas.draw_line((x + 500, y), (0, 0), 11, "Black")

        canvas.draw_line((ya - 500, ya), (600, 600), 10, "Cyan")
        canvas.draw_line((ya, ya - 500), (600, 600), 10, "#88D4F5")
        
        canvas.draw_circle((300, ya), 50, 1, "Yellow", "Yellow")
        if(ya <= 5):
            ya = 600
            y = 5
            y = y + 5
    
    if(x >= 600):
        global xa
        xa = xa - 5
        canvas.draw_circle((xa, 300), 50, 1, "Green", "Green")        

        if(xa <= 5):
            xa = 600
            x = 5
            x = x + 5
           

frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler)
frame.start()
