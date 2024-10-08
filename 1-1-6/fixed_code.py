#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
# refactor --> rename
spider_body = trtl.Turtle()
spider_body.pensize(40)
spider_body.circle(20)

amount_legs = 8
leg_length = 70
space_between_legs = 360 / amount_legs

spider_body.pensize(5)
increments = 0
while (increments < amount_legs):
  spider_body.goto(0,20)
  spider_body.setheading(space_between_legs * increments)
  spider_body.forward(leg_length)
  increments = increments + 1
spider_body.hideturtle()

wn = trtl.Screen()
wn.mainloop()