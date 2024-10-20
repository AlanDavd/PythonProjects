"""
Simulates a Spirograph.
"""

import turtle
import sys, random, argparse
import numpy as np
import math
import random
from PIL import Image
from datetime import datetime
from fractions import gcd

class Spiro:
  def __init__(self, xc, yc, col, R, r, l) -> None:
    self.t = turtle.Turtle()
    self.t.shape("turtle")
    self.step = 5
    self.drawingComplete = False

    self.setparams(xc, yc, R, r, l)
    self.restart()

  def setparams(self, xc, yc, col, R, r, l):
    # spirograph parameters
    self.xc = xc
    self.yc = yc
    self.R = int(R)
    self.r = int(r)
    self.l = l
    self.col = col
    # reduce r/R to smallest form by dividing with GCD
    gcdVal = gcd(self.r, self.R)
    self.nRot = self.r//gcdVal
    # get ratio of radii
    self.k = r/float(R)
    # set color
    self.t.color(*col)
    # current angle
    self.a = 0

  def restart(self):
    self.drawingComplete = False
    self.t.showturtle()

    # go to first point
    self.t.up()
    R, k, l = self.R, self.k, self.l
    a = 0.0
    x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
    y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
    self.t.setpos(self.xc + x, self.yc + y)
    self.t.down()

  def draw(self):
    # draw rest of points
    R, k, l = self.R, self.k, self.l
    for i in range(0, 360*self.nRot + 1, self.step):
      a = math.radians(i)
      x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
      y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
      self.t.setpos(self.xc + x, self.yc + y)
    self.t.hideturtle()

  def update(self):
    # skip if done
    if self.drawingComplete:
      return
    # increment angle
    self.a += self.step
    # draw step
    R, k, l = self.R, self.k, self.l
    # set angle
    a = math.radians(self.a)
    x = self.R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
    y = self.R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
    self.t.setpos(self.xc + x, self.yc + y)
    # check if drawing is complete and set flag
    if self.a >= 360*self.nRot:
      self.drawingComplete = True
      self.t.hideturtle()

  def clear(self):
    self.t.clear()

class SpiroAnimator:
  def __init__(self, N):
    # timer value in milliseconds
    self.deltaT = 10
    # get window dimensions
    self.width = turtle.window_width()
    self.height = turtle.window_height()
    # create spiro objects
    self.spiros = []
    for i in range(N):
      # generate random parameters
      rparams = self.genRandomParams()
      # set spiro params
      spiro = Spiro(*rparams)
      self.spiros.append(spiro)
    turtle.ontimer(self.update, self.deltaT)

  # restart sprio drawing
  def restart(self):
    for spiro in self.spiros:
      spiro.clear()
      # generate random parameters
      rparams = self.genRandomParams()
      # set spiro params
      spiro.setparams(*rparams)
      spiro.restart()

  def genRandomParams(self):
    width, height = self.width, self.height
    R = random.randint(50, min(width, height)//2)
    r = random.randint(10, 9*R//10)
    l = random.uniform(0.1, 0.9)
    xc = random.randint(-width//2, width//2)
    yc = random.randint(-height//2, height//2)
    col = (random.random(),
            random.random(),
            random.random())
    return (xc, yc, col, R, r, l)

  def update(self):
    # update all spiros
    nComplete = 0
    for spiro in self.spiros:
      spiro.update()
      # count completed ones
      if spiro.drawingComplete:
        nComplete+= 1
    # if all spiros are complete, restart
    if nComplete == len(self.spiros):
      self.restart()
    turtle.ontimer(self.update, self.deltaT)

  # toggle turtle on/off
  def toggleTurtles(self):
    for spiro in self.spiros:
      if spiro.t.isvisible():
        spiro.t.hideturtle()
      else:
        spiro.t.showturtle()

# save spiros to image
def saveDrawing():
  turtle.hideturtle()
  # generate unique file name
  dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
  fileName = 'spiro-' + dateStr 
  print('saving drawing to %s.eps/png' % fileName)
  # get tkinter canvas
  canvas = turtle.getcanvas()
  # save postscipt image
  canvas.postscript(file = fileName + '.eps')
  # use PIL to convert to PNG
  img = Image.open(fileName + '.eps')
  img.save(fileName + '.png', 'png')
  turtle.showturtle()

# main() function
def main():
  # use sys.argv if needed
  print('generating spirograph...')
  # create parser
  descStr = """This program draws spirographs using the Turtle module. 
  When run with no arguments, this program draws random spirographs.
  
  Terminology:

  R: radius of outer circle.
  r: radius of inner circle.
  l: ratio of hole distance to r.
  """
  parser = argparse.ArgumentParser(description=descStr)

  # add expected arguments
  parser.add_argument('--sparams', nargs=3, dest='sparams', required=False, 
                      help="The three arguments in sparams: R, r, l.")

  # parse args
  args = parser.parse_args()

  # set to 80% screen width
  turtle.setup(width=0.8)

  # set cursor shape
  turtle.shape('turtle')

  # set title
  turtle.title("Spirographs!")
  # add key handler for saving images
  turtle.onkey(saveDrawing, "s")
  # start listening 
  turtle.listen()

  # hide main turtle cursor
  turtle.hideturtle()

  # checks args and draw
  if args.sparams:
    params = [float(x) for x in args.sparams]
    # draw spirograph with given parameters
    # black by default
    col = (0.0, 0.0, 0.0)
    spiro = Spiro(0, 0, col, *params)
    spiro.draw()
  else:
    # create animator object
    spiroAnim = SpiroAnimator(4)
    # add key handler to toggle turtle cursor
    turtle.onkey(spiroAnim.toggleTurtles, "t")
    # add key handler to restart animation
    turtle.onkey(spiroAnim.restart, "space")

  # start turtle main loop
  turtle.mainloop()

# call main
if __name__ == '__main__':
  main()