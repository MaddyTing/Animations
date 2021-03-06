#Animation with Tom and Jerry

import simplegui
import random

j = 350  #Jerry's starting position
x = 0
y = -350
xa = -350
a = -200
b = 0
c = -50
ya = 0

message = "Tom and Jerry"
message1j = "I stole Tom's apple!"
message2t = "Get back here!"
message2j = "Catch me if you can!"
message3t1 = "Give me my apple!"
message3j1 = "Please don't hurt me!"
message4t = "I'm so tired..."
message4j = "Haha! I win!"

messages = ["Tom and Jerry"]
charactermessages = [message4t, message4j]

def draw_handler(canvas):
    for sceneall in messages:           
        canvas.draw_text(message, [300,100], 100, "Yellow")
    
#SCENE 1
    global x
    global y
    x = 150
    y = y + 10
    
    if (y < 0):
        #JERRY
        #Ears
        canvas.draw_polygon([(j - 30, j - 20), (j - 60, j), (j - 70, j - 50)], 10, "#663333", "#663333")
        canvas.draw_polygon([(j + 30, j - 20), (j + 60, j), (j + 70, j - 50)], 10, "#663333", "#663333")
        #Inner Ears
        canvas.draw_polygon([(j - 20, j - 10), (j - 50, j + 10), (j - 60, j - 30)], 10, "#E4A6A6", "#E4A6A6")
        canvas.draw_polygon([(j + 20, j - 10), (j + 50, j + 10), (j + 60, j - 30)], 10, "#E4A6A6", "#E4A6A6")
        #Face
        canvas.draw_circle((j, j), 60, 10, "#805555", "#805555")
        #Eyes
        canvas.draw_circle((j + 40, j), 10, 10, "black", "black")
        canvas.draw_circle((j - 40, j), 10, 10, "black", "black")
        #Mouth
        canvas.draw_circle((j, j), 20, 10, "black", "black")
        canvas.draw_polygon([(j - 20, j - 40), (j + 20, j - 40),(j + 20, j - 20), (j - 20, j - 20)], 10, "#805555", "#805555")

        #APPLE
        canvas.draw_circle((j, j + 60), 20, 5, "red", "red")

        canvas.draw_text(message1j, [300,200], 50, "White")
    
#SCENE 2    
    
   
    #JERRY   
    #Ears
    canvas.draw_polygon([(x - 30, y - 20), (x - 60, y), (x - 70, y - 50)], 10, "#663333", "#663333")
    canvas.draw_polygon([(x + 30, y - 20), (x + 60, y), (x + 70, y - 50)], 10, "#663333", "#663333")
    #Inner Ears
    canvas.draw_polygon([(x - 20, y - 10), (x - 50, y + 10), (x - 60, y - 30)], 10, "#E4A6A6", "#E4A6A6")
    canvas.draw_polygon([(x + 20, y - 10), (x + 50, y + 10), (x + 60, y - 30)], 10, "#E4A6A6", "#E4A6A6")
    #Face
    canvas.draw_circle((x, y), 60, 10, "#805555", "#805555")
    #Eyes
    canvas.draw_circle((x + 40, y), 10, 10, "black", "black")
    canvas.draw_circle((x - 40, y), 10, 10, "black", "black")
    #Mouth
    canvas.draw_circle((x, y), 20, 10, "black", "black")
    canvas.draw_polygon([(x - 20, y - 40), (x + 20, y - 40),(x + 20, y - 20), (x - 20, y - 20)], 10, "#805555", "#805555")

    #APPLE
    canvas.draw_circle((x, y + 60), 20, 5, "red", "red")

    #TOM    
    if(y >= 320):
        #Ears
        canvas.draw_polygon([(x - 70, y - 350), (x - 50, y - 430), (x - 20, y - 380)], 10, "#3D3D3D", "#3D3D3D")
        canvas.draw_polygon([(x + 70, y - 350), (x + 50, y - 430), (x + 20, y - 380)], 10, "#3D3D3D", "#3D3D3D")
        #Inner Ears
        canvas.draw_polygon([(x - 60, y - 350), (x - 45, y - 400), (x - 30, y - 380)], 10, "#C38989", "#C38989")
        canvas.draw_polygon([(x + 60, y - 350), (x + 45, y - 400), (x + 30, y - 380)], 10, "#C38989", "#C38989")
        #Face
        canvas.draw_circle((x, y - 320), 80, 10, "gray", "gray")
        #Eyes
        canvas.draw_circle((x + 30, y - 320), 10, 10, "black", "black")
        canvas.draw_circle((x - 30, y - 320), 10, 10, "black", "black")
        #Eyebrows
        canvas.draw_line((x + 10, y - 330), (x + 30, y - 390), 10, "black")
        canvas.draw_line((x - 10, y - 330), (x - 30, y - 390), 10, "black")
        #Whiskers (Right)
        canvas.draw_line((x + 30, y - 290), (x + 100, y - 320), 10, "#3D3D3D")
        canvas.draw_line((x + 30, y - 290), (x + 100, y - 280), 10, "#3D3D3D")
        canvas.draw_line((x + 30, y - 290), (x + 80, y - 240), 10, "#3D3D3D")
        #Whiskers (Left)
        canvas.draw_line((x - 30, y - 290), (x - 100, y - 320), 10, "#3D3D3D")
        canvas.draw_line((x - 30, y - 290), (x - 100, y - 280), 10, "#3D3D3D")
        canvas.draw_line((x - 30, y - 290), (x - 80, y - 240), 10, "#3D3D3D")
        #Mouth
        canvas.draw_circle((x, y - 280), 20, 10, "black", "black")
        canvas.draw_polygon([(x - 20, y - 250), (x + 20, y - 250), (x + 20, y - 250), (x - 20, y - 250)], 10, "gray", "gray")
        
        if(y < 1500):          
            canvas.draw_text(message2t, [300,150], 50, "White")
            canvas.draw_text(message2j, [300,200], 50, "Black")

#SCENE 3            
        if(y >= 1500):
            global xa
            global ya
            xa = xa + 7
            ya = 700
            #JERRY  
            #Ears
            canvas.draw_polygon([(xa + 240, ya - 330), (xa + 230, ya - 400), (xa + 310, ya - 350)], 10, "#663333", "#663333")
            canvas.draw_polygon([(xa + 300, ya - 350), (xa + 370, ya - 400), (xa + 360, ya - 330)], 10, "#663333", "#663333")
            #Inner Ears
            canvas.draw_polygon([(xa + 250, ya - 310), (xa + 240, ya - 380), (xa + 320, ya - 330)], 10, "#C38989", "#C38989")
            canvas.draw_polygon([(xa + 290, ya - 330), (xa + 360, ya - 380), (xa + 350, ya - 310)], 10, "#C38989", "#C38989")
            #Face
            canvas.draw_circle((xa + 300, ya - 320), 60, 10, "#805555", "#805555")
            #Eyes
            canvas.draw_circle((xa + 340, ya - 320), 10, 10, "black", "black")
            canvas.draw_circle((xa + 260, ya - 320), 10, 10, "black", "black")
            #Mouth
            canvas.draw_circle((xa + 300, ya - 320), 20, 10, "black", "black")
            canvas.draw_polygon([(xa + 280, ya - 300), (xa + 320, ya - 300),(xa + 320, ya - 300), (xa + 280, ya - 300)], 10, "#805555", "#805555")
            
            #APPLE
            canvas.draw_circle((xa + 300, ya - 270), 20, 5, "red", "red")
            
            #TOM
            #Ears
            canvas.draw_polygon([(xa - 70, ya - 350), (xa - 50, ya - 430), (xa - 20, ya - 380)], 10, "#3D3D3D", "#3D3D3D")
            canvas.draw_polygon([(xa + 70, ya - 350), (xa + 50, ya - 430), (xa + 20, ya - 380)], 10, "#3D3D3D", "#3D3D3D")
            #Inner Ears
            canvas.draw_polygon([(xa - 60, ya - 350), (xa - 45, ya - 400), (xa - 30, ya - 380)], 10, "#C38989", "#C38989")
            canvas.draw_polygon([(xa + 60, ya - 350), (xa + 45, ya - 400), (xa + 30, ya - 380)], 10, "#C38989", "#C38989")
            #Face
            canvas.draw_circle((xa, ya - 320), 80, 10, "gray", "gray")
            #Eyes
            canvas.draw_circle((xa + 30, ya - 320), 10, 10, "black", "black")
            canvas.draw_circle((xa - 30, ya - 320), 10, 10, "black", "black")
            #Eyebrows
            canvas.draw_line((xa + 10, ya - 330), (xa + 30, ya - 390), 10, "black")
            canvas.draw_line((xa - 10, ya - 330), (xa - 30, ya - 390), 10, "black")
            #Whiskers (Right)
            canvas.draw_line((xa + 30, ya - 290), (xa + 100, ya - 320), 10, "#3D3D3D")
            canvas.draw_line((xa + 30, ya - 290), (xa + 100, ya - 280), 10, "#3D3D3D")
            canvas.draw_line((xa + 30, ya - 290), (xa + 80, ya - 240), 10, "#3D3D3D")
            #Whiskers (Left)
            canvas.draw_line((xa - 30, ya - 290), (xa - 100, ya - 320), 10, "#3D3D3D")
            canvas.draw_line((xa - 30, ya - 290), (xa - 100, ya - 280), 10, "#3D3D3D")
            canvas.draw_line((xa - 30, ya - 290), (xa - 80, ya - 240), 10, "#3D3D3D")
            #Mouth
            canvas.draw_circle((xa, ya - 280), 20, 10, "black", "black")
            canvas.draw_polygon([(xa - 20, ya - 250), (xa + 20, ya - 250), (xa + 20, ya - 250), (xa - 20, ya - 250)], 10, "gray", "gray")

            if(xa <= 1000):
                canvas.draw_text(message3t1, [300,150], 50, "White")
                canvas.draw_text(message3j1, [300, 200], 50, "Black")
                

#SCENE 4
        if(xa >= 1300):
            global a
            global b
            global c
            a = a + 5  #x/xa replacement
            b = 700  #y/ya replacement
            c = c + 2  #a replacement for slow tom

            #JERRY 
            #Ears
            canvas.draw_polygon([(a + 240, b - 330), (a + 230, b - 400), (a + 310, b - 350)], 10, "#663333", "#663333")
            canvas.draw_polygon([(a + 300, b - 350), (a + 370, b - 400), (a + 360, b - 330)], 10, "#663333", "#663333")
            #Inner Ears
            canvas.draw_polygon([(a + 250, b - 310), (a + 240, b - 380), (a + 320, b - 330)], 10, "#C38989", "#C38989")
            canvas.draw_polygon([(a + 290, b - 330), (a + 360, b - 380), (a + 350, b - 310)], 10, "#C38989", "#C38989")
            #Face
            canvas.draw_circle((a + 300, b - 320), 60, 10, "#805555", "#805555")
            #Eyes
            canvas.draw_circle((a + 340, b - 320), 10, 10, "black", "black")
            canvas.draw_circle((a + 260, b - 320), 10, 10, "black", "black")
            #Mouth
            canvas.draw_circle((a + 300, b - 320), 20, 10, "black", "black")
            canvas.draw_polygon([(a + 280, b - 340), (a + 320, b - 340),(a + 320, b - 340), (a + 280, b - 340)], 10, "#805555", "#805555")
            
            #APPLE
            canvas.draw_circle((a + 300, b - 270), 20, 5, "red", "red")
            
            #SLOW TOM
            #Ears
            canvas.draw_polygon([(c - 70, b - 350), (c - 50, b - 430), (c - 20, b - 380)], 10, "#3D3D3D", "#3D3D3D")
            canvas.draw_polygon([(c + 70, b - 350), (c + 50, b - 430), (c + 20, b - 380)], 10, "#3D3D3D", "#3D3D3D")
            #Inner Ears
            canvas.draw_polygon([(c - 60, b - 350), (c - 45, b - 400), (c - 30, b - 380)], 10, "#C38989", "#C38989")
            canvas.draw_polygon([(c + 60, b - 350), (c + 45, b - 400), (c + 30, b - 380)], 10, "#C38989", "#C38989")
            #Face
            canvas.draw_circle((c, b - 320), 80, 10, "gray", "gray")
            #Eyes
            canvas.draw_circle((c + 30, b - 320), 10, 10, "black", "black")
            canvas.draw_circle((c - 30, b - 320), 10, 10, "black", "black")
            #Eyebrows
            canvas.draw_line((c + 20, b - 360), (c + 30, b - 350), 10, "black")
            canvas.draw_line((c - 20, b - 360), (c - 30, b - 350), 10, "black")
            #Whiskers (Right)
            canvas.draw_line((c + 30, b - 290), (c + 100, b - 320), 10, "#3D3D3D")
            canvas.draw_line((c + 30, b - 290), (c + 100, b - 280), 10, "#3D3D3D")
            canvas.draw_line((c + 30, b - 290), (c + 80, b - 240), 10, "#3D3D3D")
            #Whiskers (Left)
            canvas.draw_line((c - 30, b - 290), (c - 100, b - 320), 10, "#3D3D3D")
            canvas.draw_line((c - 30, b - 290), (c - 100, b - 280), 10, "#3D3D3D")
            canvas.draw_line((c - 30, b - 290), (c - 80, b - 240), 10, "#3D3D3D")
            #Mouth
            canvas.draw_circle((c, b - 280), 20, 10, "black", "black")
            canvas.draw_polygon([(c - 20, b - 250), (c + 20, b - 250), (c + 20, b - 250), (c - 20, b - 250)], 10, "gray", "gray")

            for scenefour in charactermessages:
                canvas.draw_text(message4t, [300,150], 50, "White")
                canvas.draw_text(message4j, [300,200], 50, "Black")
                
    if(c >= 1000):
         canvas.draw_text("THE END", [300,400], 100, "White")
            
frame = simplegui.create_frame('Testing', 900, 900)
frame.set_canvas_background("green")
frame.set_draw_handler(draw_handler)
frame.start()
