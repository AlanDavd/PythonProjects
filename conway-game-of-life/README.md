# Conway’s Game of Life

The Game of Life is an example of a cellular automaton, a collection of colored cells on a
grid that evolve through a number of time steps according to a set of rules defining the
states of neighboring cells.

It is used to study a system by creating a mathematical model for that system, writing a
program to represent the model, and then letting the model evolve over time. There are many
kinds of computer simulations, but this once focuses on the work of the British
mathematician John Conway.

This simulation consists of the following components:
• A property defined in one or two dimensional space
• A mathematical rule to change this property for each step in the simulation
• A way to display or capture the state of the system as it evolves

The cells in Conway’s Game of Life can be either ON or OFF. The game starts with an
initial condition, in which each cell is assigned one state and mathematical rules determine
how its state will change over time. Patterns include “gliders” that slide across the grid,
“blinkers” that flash on and off, and even replicating patterns.

Conway’s Game of Life has four rules:

1. If a cell is ON and has fewer than two neighbors that are ON, it turns OFF.
2. If a cell is ON and has either two or three neighbors that are ON, it remains ON.
3. If a cell is ON and has more than three neighbors that are ON, it turns OFF.
4. If a cell is OFF and has exactly three neighbors that are ON, it turns ON.

These rules are meant to mirror some basic ways that a group of organisms might fare over
time: underpopulation and overpopulation kill cells by turning a cell OFF when it has fewer
than two neighbors or more than three, and cells stay ON and reproduce by turning another cell
from OFF to ON when the population is balanced.

# Usage

## Create Virtual Environment and Install Dependencies

```bash
python3 -m venv venv # create a new venv in ./venv
source source venv/bin/activate # activate your new venv
```

## Run

Pressing S saves the drawing.

```bash
$ python conway.py

$ python conway.py --grid-size 32 --interval 500 --glider # Enter parameters for a particular draw
```
