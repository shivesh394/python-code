import itertools
from collections import Counter
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(list(itertools.chain.from_iterable(board)))
word_dict = Counter(word)
board_dict = Counter(itertools.chain.from_iterable(board))   
if any(board_dict[char] < count for char, count in word_dict.items()):
    print(False)
else:
    print(True)