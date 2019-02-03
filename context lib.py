from time import perf_counter
from array import array
from contextlib import contextmanager

@contextmanager  2
def timing(label: str):
    t0 = perf_counter()  3
    yield lambda: (label, t1 - t0)  4
    t1 = perf_counter() 5

with timing('Array tests') as total:  7
    with timing('Array creation innermul') as inner:
        x = array('d', [0] * 1000000)  1

    with timing('Array creation outermul') as outer:
        x = array('d', [0]) * 1000000  6


print('Total [%s]: %.6f s' % total())
print('    Timing [%s]: %.6f s' % inner())
print('    Timing [%s]: %.6f s' % outer())
