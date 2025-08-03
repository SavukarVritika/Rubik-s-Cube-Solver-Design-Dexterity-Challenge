
import copy
import time

# Define moves: U, D, L, R, F, B and their clockwise rotations
MOVES = ['U', "U'", 'D', "D'", 'L', "L'", 'R', "R'", 'F', "F'", 'B', "B'"]

# Cube face indices: U, D, L, R, F, B
FACES = ['U', 'D', 'L', 'R', 'F', 'B']

class RubiksCube:
    def __init__(self):
        self.state = {face: [face]*9 for face in FACES}  # each face has 9 stickers

    def copy(self):
        return copy.deepcopy(self)

    def is_solved(self):
        return all(len(set(self.state[face])) == 1 for face in FACES)

    def apply_move(self, move):
       
        pass  

    def scramble(self, moves):
        for move in moves:
            self.apply_move(move)
def heuristic(cube):
    
    cost = 0
    for face in FACES:
        cost += sum(1 for s in cube.state[face] if s != face)
    return cost // 8  
def ida_star(cube):
    threshold = heuristic(cube)
    path = []
    def search(node, g, prev_move, threshold):
        f = g + heuristic(node)
        if f > threshold:
            return f
        if node.is_solved():
            return 'FOUND'
        min_threshold = float('inf')
        for move in MOVES:
            if move == prev_move: 
                continue
            new_node = node.copy()
            new_node.apply_move(move)
            path.append(move)
            t = search(new_node, g + 1, move, threshold)
            if t == 'FOUND':
                return 'FOUND'
            if t < min_threshold:
                min_threshold = t
            path.pop()
        return min_threshold

    while True:
        t = search(cube, 0, None, threshold)
        if t == 'FOUND':
            return path
        if t == float('inf'):
            return None
        threshold = t


if __name__ == '__main__':
    cube = RubiksCube()
    scramble_seq = ['R', "U'", 'F', 'L', "D'", 'B']
    cube.scramble(scramble_seq)

    print("Scrambled cube with:", scramble_seq)
    start = time.time()
    solution = ida_star(cube)
    end = time.time()

    print("Solution:", solution)
    print(f"Solved in {len(solution)} moves. Time: {end - start:.2f}s")
