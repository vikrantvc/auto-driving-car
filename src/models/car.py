from src.utils.directions import Direction

class Car():
    def __init__(self, name: str, x: int, y: int, direction: Direction, commands: str):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands
        
    def rotate_left(self):
        rotation_map = {
            Direction.EAST: Direction.NORTH,
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST,
        }

        self.direction = rotation_map[self.direction]

    def rotate_right(self):
        rotation_map = {
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH,
            Direction.NORTH: Direction.EAST,
        }

        self.direction = rotation_map[self.direction]
        
    def move_forward(self, max_x, max_y):

        if self.direction == Direction.EAST:
            self.x = min(self.x + 1, max_x)
        elif self.direction == Direction.WEST:
            self.x = max(self.x - 1, 0)
        elif self.direction == Direction.NORTH:
            self.y = min(self.y + 1, max_y)
        elif self.direction == Direction.SOUTH:
            self.y = max(self.y - 1, 0)

