import psutil
import os, sys, time

pid = os.getpid()  1
p = psutil.Process(pid)  2
print('Process info:')
print('  name  :', p.name())
print('  exe   :', p.exe())

data = []
while True:
    data += list(range(100000))  3
    info = p.memory_full_info()
    # Convert to MB
    memory = info.uss / 1024 / 1024
    print('Memory used: {:.2f} MB'.format(memory))
    if memory > 40:
        print('Memory too big! Exiting.')
        sys.exit()
    time.sleep(1)
