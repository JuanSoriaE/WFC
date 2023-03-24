import random

OFFS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

def getStateFromNeighbors(grid: list[list[list]], r: int, c: int, collapsed: list[list[bool]], TOTAL: set) -> int:
    N, M = len(grid), len(grid[0])
    cnt = {state: 0 for state in TOTAL}

    for x, y in OFFS:
        new_r, new_c = r + y, c + x
        if min(new_r, new_c) < 0 or new_r >= N or new_c >= M or not collapsed[new_r][new_c]:
            continue
        
        cnt[grid[new_r][new_c][0]] += 1

    choices: list = []
    for state in TOTAL:
        if state in grid[r][c]:
            choices += [state for i in range(cnt[state])]
    
    choices += grid[r][c]
    return random.choice(choices)
