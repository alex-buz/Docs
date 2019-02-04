```Python
# cython: boundscheck=False, cdivision=True
import array
import threading  1

cpdef void target(double[:] piece) nogil:  2
    cdef int i, n = piece.shape[0]
    with nogil:  3
        for i in range(n):
            piece[i] = i % 3


cdef int n = int(1e8)  4
cdef object a = array.array('d', [0.0]) * n


view = memoryview(a)  5
piece_size = int(n / 2)  6

thread1 = threading.Thread(  7
    target=target,
    args=(view[:piece_size],)
)

thread2 = threading.Thread(
    target=target,
    args=(view[piece_size:],)
)

thread1.start()  8
thread2.start()

thread1.join()  9
thread2.join()

print(a[:5])
```
```
$ cythonize -b -i -a cythondemopll.pyx
```

Create exec
```
$ cython --embed cythondemopll.pyx
```



```
$ gcc `python3.5-config --cflags` cythondemopll.c \
      `python3.5-config --ldflags` -o cythondemopll
```
