
```Python
import arrow

t0 = arrow.now()
print(t0)

t1 = arrow.utcnow()
print(t1)

difference = (t0 - t1).total_seconds()

print('Total difference: %.2f seconds' % difference)
```



Also `pytz`


```
import parsedatetime as pdt

cal = pdt.Calendar()

examples = [
    "2016-07-16",
    "2016/07/16",
    "2016-7-16",
    "2016/7/16",
    "07-16-2016",
    "7-16-2016",
    "7-16-16",
    "7/16/16",
]

print('{:30s}{:>30s}'.format('Input', 'Result'))
print('=' * 60)
for e in examples:
    dt, result = cal.parseDT(e)
    print('{:<30s}{:>30}'.format('"' + e + '"', dt.ctime()))
```
```Python
import parsedatetime as pdt
from datetime import datetime

cal = pdt.Calendar()

examples = [
    "19 November 1975",
    "19 November 75",
    "19 Nov 75",
    "tomorrow",
    "yesterday",
    "10 minutes from now",
    "the first of January, 2001",
    "3 days ago",
    "in four days' time",
    "two weeks from now",
    "three months ago",
    "2 weeks and 3 days in the future",
]

print('Now: {}'.format(datetime.now().ctime()), end='\n\n')
print('{:40s}{:>30s}'.format('Input', 'Result'))
print('=' * 70)
for e in examples:
    dt, result = cal.parseDT(e)
    print('{:<40s}{:>30}'.format('"' + e + '"', dt.ctime()))
 ```
Also `Chronyk`
