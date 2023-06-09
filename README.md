# WFC

Wave Function Algorithm implementation written in Python.

## Usage

### Installation

You must have Python installed.
Just clone this repository since the implementation only uses pre-installed packages.
```
git clone https://github.com/JuanSoriaE/WFC.git
```

Then import the module in the Python file you will use it.
```
from WFC import wfc
```

Call the function `WFC` from `wfc` module.

### INPUT

Here is the list of the parameters of `WFC` function:

| Name | Type | Description | Required | Example |
| ---- | ---- | ----------- | -------- | ------- |
| ini_state | list | Initial state that all the cells will have (Must contain all the possible states). | Yes | `[0, 1, 2]` |
| n | int | Number of rows of the grid. | Yes | `10` |
| m | int | Number of colums of the grid. | Yes | `10` |
| adj_dic | dict | Adjacency dictionary, which states can be adjacent to which other states. | Yes | `{0: [0, 1], 1: [0, 1, 2], 2: [1, 2]}` |
| ini_cell | tuple | Inicial cell to collapse (`(0, 0)` by default). | No | `(5, 7)` |
| adj_offs | list[tuple] | Coordinates of adjacents offsets (`[(0, -1), (1, 0), (0, 1), (-1, 0)]` by default). | No | `[(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]` |
| neighbors_based | bool | If you want to collapse the state based on the state of the collapsed neighbors (`False` by default). | No | `True` |

Example of function call.
```
offs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

output = grid = wfc.WFC([0, 1, 2], 50, 50, {0: [0, 1], 1: [0, 1, 2], 2: [1, 2]}, (0, 0), offs, True)
```

### OUTPUT

The return value will be a list of lists which contains a list with a single value (the final state).
```
output = [[[0], [0], [1], [1]],
          [[0], [1], [1], [1]],
          [[1], [1], [0], [1]],
          [[1], [0], [1], [1]]]
```

## Examples


