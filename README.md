# WFC

Wave Function Algorithm implementation written in Python.

## Usage

### Installation

You must have Python installed.
Just clone this repository since the implementation only uses pre-installed packages.

Import the module in the Python file you will use it.
```
import wfc
```

Call the function `WFC` from `wfc` module.

### INPUT

Here is the list of the paramters of `WFC` function:

| Name | Type | Description | Required | Example |
| ---- | ---- | ----------- | -------- | ------- |
| ini_state | list | Initial state that all the cells will have (Must to contain all the possible states). | Yes | `[0, 1, 2]` |
| n | int | Number of rows of the grid. | Yes | `10` |
| m | int | Number of colums of the grid. | Yes | `10` |
| adj_dict | dic | Adjacency dictionary, which states can be adjacent to which other states. | Yes | `{0: [0, 1], 1: [0, 1, 2], 2: [1, 2]}` |
| neighbors_based | bool | If you want to collapse the state based on the state of the collapsed neighbors (`False` by default). | No | `True` |

Example of function call.
```
grid = wfc.WFC(3, [0, 1, 2], 50, 50, {0: [0, 1], 1: [0, 1, 2], 2: [1, 2]}, True)
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


