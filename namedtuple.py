from collections import namedtuple

Bite = namedtuple('Bite', ['number', 'title', 'is_complex'])

def make_namedtuple(number, title, score):
    bite = Bite(
        number = number,
        title = title,
        is_complex = score > 5
    )
    return bite


bite = make_namedtuple(1, 'first bite', 6)
print(bite)