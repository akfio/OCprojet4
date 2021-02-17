from operator import itemgetter
import numpy

player = [
    ("Brady", "Tom", "03/06/1960", "H", 1),
    ("James", "LeBron", "03/06/1960", "H", 3),
    ("Westbrook", "Russell", "03/06/1960", "H", 7),
    ("Federer", "Roger", "03/06/1960", "H", 8),
    ("Nadal", "Rapha", "03/06/1960", "H", 5),
    ("Henry", "Titi", "03/06/1960", "H", 4),
    ("Gignac", "André", "03/06/1960", "H", 6),
    ("Obama", "Presi", "03/06/1960", "H", 2)
]


def get_rencontres():
    a = itemgetter(4)
    b = sorted(player, key=a)
    c = len(b) // 2
    first_half = b[:c]
    second_half = b[c:]
    first_round = [
        (first_half[0][0:2], "vs", second_half[0][0:2]),
        (first_half[1][0:2], "vs", second_half[1][0:2]),
        (first_half[2][0:2], "vs", second_half[2][0:2]),
        (first_half[3][0:2], "vs", second_half[3][0:2])
    ]
    return first_round



get_rencontres()
