

```Python
>>> from sortedcontainers import SortedList
>>> sl = SortedList(['e', 'a', 'c', 'd', 'b'])
>>> sl
SortedList(['a', 'b', 'c', 'd', 'e'])
>>> sl *= 10_000_000
>>> sl.count('c')
10000000
>>> sl[-3:]
['e', 'e', 'e']
>>> from sortedcontainers import SortedDict
>>> sd = SortedDict({'c': 3, 'a': 1, 'b': 2})
>>> sd
SortedDict({'a': 1, 'b': 2, 'c': 3})
>>> sd.popitem(index=-1)
('c', 3)
>>> from sortedcontainers import SortedSet
>>> ss = SortedSet('abracadabra')
>>> ss
SortedSet(['a', 'b', 'c', 'd', 'r'])
>>> ss.bisect_left('c')
```
