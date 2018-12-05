import items

LEVELS = [
    {
        'stack': [1, 2, 1, 2, 3, 2, 1, 1],
        'room': [
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, -1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]
        ],
        'spr': (0, 0)
    },
    {
        'stack': [2, 3, 3, 2, 3, 2, 1, 1],
        'room': [
            [0, 2, 0, 0, 4, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, -1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]
        ],
        'spr': (0, 288)
    },
    {
        'stack': [3, 3, 3, 3, 3, 3, 3, 3],
        'room': [
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, -1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 4, 0, 0, 0, 0, 3]
        ],
        'spr': (224, 144)
    }
]


def setup_tiles(storage, level=0):
    storage['room'] = [[None] * 12 for _ in range(7)]
    for i, line in enumerate(LEVELS[level]['room']):
        for j, t in enumerate(line):
            item = items.ITEMS_MAPPING[t]()
            print("Created {} [{},{}]".format(item, i, j))
            storage['room'][i][j] = item


def store_tile(storage, item, x, y):
    print("item={} x={} y={}".format(item, x, y))
    storage['room'][y][x] = item


def can_store_tile(storage, x, y):
    return storage['room'][y][x].type == 0


def get_tiles(storage):
    return storage['room']
