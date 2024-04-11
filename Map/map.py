from random import randint, seed

class Tile:
    def __init__(self, symbol: str, color: str | None = None):
        self.symbol = f"{color}{symbol}{ANSI_RESET}" if color else symbol

ANSI_RESET = "\033[0m"
ANSI_YELLOW = "\033[33m"
ANSI_GREEN = "\033[32m"
ANSI_BLUE = "\033[34m"
ANSI_RED = "\033[31m"
ANSI_WHITE = "\033[97m"
ANSI_MAGENTA = "\033[35m"
ANSI_CYAN = "\033[36m"

plains = Tile(".", ANSI_YELLOW)
forest = Tile("8", ANSI_GREEN)
pines = Tile("Y", ANSI_GREEN)
mountain = Tile("A", ANSI_WHITE)
water = Tile("~", ANSI_CYAN)
player = Tile("P", ANSI_RED)

class Map:
    def __init__(self, width: int, height: int, seed: int, hero) -> None:
        self.width = width
        self.height = height
        self.seed = seed

        self.map_data: list[list[Tile]]
        self.full_map = []

        self.generate_map()
        self.generate_patch(forest, 1, 5, 7)
        self.generate_patch(pines, 0, 2, 5)
        self.generate_patch(mountain, 3, 5, 7)
        self.generate_patch(water, 1, 5, 8)

        self.construct_map(player_x=hero.x, player_y=hero.y)

    def generate_map(self) -> None:
        if self.seed is not None:
            seed(self.seed)  # Configurando a semente para o gerador de números aleatórios

        self.map_data = [[plains for _ in range(self.width)] for _ in range(self.height)]

    def generate_patch(
            self,
            tile: Tile,
            num_patches: int,
            min_size: int,
            max_size: int,
            irregular: bool = True
    ) -> None:
        for _ in range(num_patches):
            width = randint(min_size, max_size)
            height = randint(min_size, max_size)
            start_x = randint(1, self.width - width - 1)
            start_y = randint(1, self.height - height - 1)

            if irregular:
                init_start_x = randint(3, self.width - max_size)

            for i in range(height):
                if irregular:
                    width = randint(int(0.7 * max_size), max_size)
                    start_x = init_start_x - randint(1, 2)
                for j in range(width):
                    self.map_data[start_y + i][start_x + j] = tile

    def construct_map(self, player_x, player_y) -> None:
        full_row = ""
        frame = "x" + self.width * "=" + "x"
        self.full_map = []

        self.full_map.append(frame)
        for y, row in enumerate(self.map_data):
            row_tiles = []
            for x, tile in enumerate(row):
                if x == player_x and y == player_y:
                    row_tiles.append(player.symbol)
                else:
                    row_tiles.append(tile.symbol)
                    full_row = "|" + "".join(row_tiles) + "|"
            self.full_map.append(full_row)
        self.full_map.append(frame)

    def display_map(self):
        for row in self.full_map:
            print(row)
