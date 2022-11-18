# A simple drawing program.
# Click on a color then click on the screen
# To draw lines of that color. The gray color will allow you to move the turtle without drawing.
# made by Iron Man FF

from turtle import *

screen = Screen()
screenMinX = -screen.window_width()/2
screenMinY = -screen.window_height()/2
screenMaxX = screen.window_width()/2
screenMaxY = screen.window_height()/2

screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)

brush_turtle = Turtle()
brush_turtle.goto(0, 0)
brush_turtle.speed(10)

def on_screen_click(x, y):
  
  if y < screenMaxY - 40:
    brush_turtle.goto(x, y)
    
screen.onclick(on_screen_click)
  

class ColorPicker(Turtle):
  def __init__(self, color="red",num=0):
    Turtle.__init__(self)
    self.num = num
    self.color_name = color
    self.speed(0)
    self.shape("circle")
    self.color("black", color)
    self.penup()
    
    self.onclick(lambda x, y: self.handle_click(x, y))

  def draw(self):
    self.setx(screenMinX+110+self.num*30)
    self.sety(screenMaxY - 20)
    
  def handle_click(self, x, y):
    if self.color_name == "#F9F9F9":
      brush_turtle.penup()
      brush_turtle.color("black")
    else:
      brush_turtle.pendown()
      brush_turtle.color(self.color_name)
    
screen.tracer(0)

ui_turtle = Turtle()
ui_turtle.ht()
ui_turtle.penup()
ui_turtle.goto(screenMinX, screenMaxY - 23)
ui_turtle.write("TurtleDraw!", align="left", font=("Courier", 10, "bold"))

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "#F9F9F9"]
color_pickers = [ColorPicker(color=c, num=i) for i, c in enumerate(colors)]
for picker in color_pickers:
  picker.draw()

screen.tracer(1)