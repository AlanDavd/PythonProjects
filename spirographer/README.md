# Spirographer

A Spirograph toy can be used to draw mathematical curves. It consists of two different sized
rings with plastic teeth, one large and one small. The small one has several holes. You put
a pen or pencil through one of the holes and then rotate the smaller wheel inside the larger
one, keeping the pen in contact with the outer wheel, to draw an endless number of complex
and wonderfully symmetric patterns.

This program is used to create an animation of Spirograph like drawing curves by using
parametric equations to describe the motion of the program’s rings and draw the curves. You’ll
be able to save the completed drawings as PNG image files and use command line options to
specify parameters or to generate random spiros.

# Usage

## Create Virtual Environment and Install Dependencies

```bash
python3 -m venv venv # create a new venv in ./venv
source source venv/bin/activate # activate your new venv

pip install -r requirements.txt
```

## Run

Pressing S saves the drawing.

```bash
$ python spiro.py # Generate random draws

$ python spiro.py --sparams 300 100 0.9 # Enter parameters for a particular draw
```
