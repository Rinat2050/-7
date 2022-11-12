Игра
с подсчётом очков!!!
https://gvard.github.io/py/turtle/









from turtle import *
listen()
shape('turtle')

def move_up():
  x = xcor()
  y = ycor()
  if abs(x) >= 50 or abs(y) >= 50:
    home()
  else:
    fd(5)

def move_down():
  x = xcor()
  y = ycor()
  if abs(x) >= 50 or abs(y) >= 50:
    home()
  else:
    bw(5)

def move_right():
  right(45)
  
def move_left():
  left(45)


# Screen().onkey(fun, key)

def up_down():
  if isdown() == True:
    penup()
  else:
    pendown()
  




Screen().onkey(move_up, 'Up')
Screen().onkey(move_down, 'Down')
Screen().onkey(move_right, 'Right')
Screen().onkey(move_left, 'Left')
Screen().onkey(up_down, 'space')
