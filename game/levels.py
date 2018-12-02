import items

LEVELS = [
    {
        'stack': [1, 2, 1, 2, 3, 2, 1, 1],
        'room': [
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]
        ]
    },
    {
        'stack': [2, 3, 3, 2, 3, 2, 1, 1],
        'room': [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    },
    {
        'stack': [3, 3, 3, 3, 3, 3, 3, 3],
        'room': [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    }
]


def setup_tiles(storage, level=0):
    storage['room'] = [[None] * 12 for _ in range(7)]
    for i, line in enumerate(LEVELS[level]['room']):
        for j, t in enumerate(line):
            item = items.ITEMS_MAPPING[t]()
            print("Created {} [{},{}]".format(item, i, j))
            storage['room'][i][j] = item


def store_tile(storage, type_, x, y):
    print("type={} x={} y={}".format(type_, x, y))
    item = items.ITEMS_MAPPING[type_]()
    storage['room'][y][x] = item


def get_tiles(storage):
    return storage['room']
