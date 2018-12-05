import random


class ItemType:
    FLOOR = 0
    BLOCK = 1
    REVERSE = 2
    RND_TURN = 3
    EXIT_POINT = 4
    SLOWER = 5
    PLAYER = -1

    @staticmethod
    def rnd():
        return random.randint(0, 5)
