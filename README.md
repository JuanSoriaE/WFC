# WFC

Wave Function Algorithm implementation written in Python

## Get started

### Installation

You must have Python installed.
Just clone this repository since the implementation only uses dependecies that comes with Python.

### Usage

Import the module in the Python file you will use it
```
import wfc
```

You just to call the function `WFC` from `wfc` module.
The function `WFC` returns a list of lists which contains a list of a single value (the final state), and receives the following parameters:

| Name | Type | Description | Required | Example |
| ---- | ---- | ----------- | -------- | ------- |
| ini_state | list | Initial state that will have all the cells in the grid (Must to contain all the possible states) | Yes | `[0, 1, 2]` |
| n | int | Number of rows of the grid | Yes | `10` |
| m | int | Number of colums of the grid | Yes | `10` |
| adj_dict | dic | Adjacency dictionary, which states can be adjacent with the state | Yes | `{0: [0, 1], 1: [0, 1, 2], 2: [1, 2]}` |
| neighbors_based | bool | If you want to collapse the state based on the states of the collapsed neighbors (`False` by default) | No | `True` |

#### Example:

Example of function call
```
grid = wfc.WFC(3, [0, 1, 2], 50, 50, {0: [0, 1], 1: [0, 1, 2], 2: [1, 2]}, True)
```
