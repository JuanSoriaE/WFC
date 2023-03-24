from WFC.utils import main as utils
from queue import Queue
import heapq
import random

OFFS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def preBuild() -> None:
    global TOTAL, grid, collapsed, heap
    TOTAL = set(INI_STATE) # set
    grid = [[INI_STATE.copy() for j in range(M)] for i in range(N)] # list[list[list]]
    collapsed = [[False for j in range(M)] for i in range(N)] # list[list[bool]]
    
    # Heap sorted by entropy
    heap = [[STATES, r, c] for r in range(N) for c in range(M)]
    heapq.heapify(heap)

def propagate(r: int, c: int) -> None:
    # Propagate contraints using Breath First Search Algorithm (BFS)
    q: Queue[tuple] = Queue()
    q.put((r, c))

    while not q.empty():
        cur_r, cur_c = q.get()
        poss_adj_states = set()

        # Get possible states
        for state in grid[cur_r][cur_c]:
            for adj_state in ADJ_DIC[state]:
                poss_adj_states.add(adj_state)
        
        # NO possible adjacent states
        no_poss_adj_states: list = list(TOTAL - poss_adj_states)

        # Remove NO possible adjacent states from the adjacent cells
        for x, y in OFFS:
            new_r, new_c = cur_r + y, cur_c + x

            # If is out of bounce or is already collapsed
            if min(new_r, new_c) < 0 or new_r >= N or new_c >= M or collapsed[new_r][new_c]:
                continue

            cell: list = grid[new_r][new_c]
            og_len: int = len(cell)
            # If the cell has a NO possible state, remove it
            for no_poss_state in no_poss_adj_states:
                if no_poss_state in cell:
                    cell.remove(no_poss_state)
                
                # If the cell collapsed
                if len(cell) == 1:
                    collapsed[new_r][new_c] = True
                    break

            if og_len != len(cell):
                q.put((new_r, new_c))
                heap.append([len(cell), new_r, new_c])

def performWFC() -> None:
    # Wave Function Collapse Algorithm
    while heap:
        e, r, c = heapq.heappop(heap)
        if collapsed[r][c]:
            continue
        
        # Collapse cell
        if NEIGHBORS_BASED:
            grid[r][c] = [utils.getStateFromNeighbors(grid, r, c, collapsed, TOTAL)]
        else:
            grid[r][c] = [random.choice(grid[r][c])]
        collapsed[r][c] = True

        # Propagate contraints
        propagate(r, c)

# MAIN
def WFC(ini_state: list, n: int, m: int, adj_dic: dict, adj_offs: list[tuple] = OFFS, neighbors_based: bool = False) -> list[list[list[int]]]:
    # Set global variables
    global STATES, INI_STATE, N, M, ADJ_DIC, NEIGHBORS_BASED, OFFS
    STATES = len(ini_state) # int
    INI_STATE = ini_state # list
    N = n # int
    M = m # int
    ADJ_DIC = adj_dic # dict
    OFFS = adj_offs
    NEIGHBORS_BASED = neighbors_based

    preBuild()

    performWFC()

    return grid
