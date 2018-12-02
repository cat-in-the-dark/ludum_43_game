import items

LEVELS = [
    {
        'stack': [items.BlockItem, items.BlockItem, items.ReverseItem, items.RandTurnItem, items.ReverseItem],
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
        'stack': [items.BlockItem, items.ReverseItem, items.ReverseItem, items.ReverseItem, items.BlockItem],
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
        'stack': [items.RandTurnItem, items.RandTurnItem, items.RandTurnItem, items.RandTurnItem, items.BlockItem],
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
    storage['room'] = [[None] * 12] * 7
    for i in range(12):
        for j in range(7):
            t = LEVELS[level]['room'][j][i]
            storage['room'][j][i] = items.ITEMS_MAPPING[t]()


def store_tile(storage, type_, x, y):
    print("{} {} {}".format(type_, x, y))
    storage['room'][x][y] = items.ITEMS_MAPPING[type_]()


def get_tiles(storage):
    return storage['room']
