SINGLE_VALUES1 = [0, 1, 2, 3, 4]
SINGLE_VALUES2 = [1, 22, 333, 69, 420]
DOUBLE_VALUES = [[0, 1], [1, 2], [7, 3], [69, 420]]
TRIPLE_VALUES = [[2, 1, 0], [7, 3, 4], [69, 420, 42]]
DIFFERENT_LISTS = [
    [1],
    SINGLE_VALUES1,
    SINGLE_VALUES2,
    *DOUBLE_VALUES,
    *TRIPLE_VALUES,
]

DIFFERENT_LISTS_WITH_EMPTY = [[]] + DIFFERENT_LISTS
