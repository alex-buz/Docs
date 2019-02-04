```Python
import json
import shelve
import atexit
from random import choice
from string import punctuation
from vocabulary import Vocabulary as vb


blank_space = """
Nice to meet you, where you been?
I could show you incredible things
Magic, madness, heaven, sin
Saw you there and I thought
Oh my God, look at that face
You look like my next mistake
Love's a game, wanna play?

New money, suit and tie
I can read you like a magazine
Ain't it funny, rumors fly
And I know you heard about me
So hey, let's be friends
I'm dying to see how this one ends
Grab your passport and my hand
I can make the bad guys good for a weekend
"""

from boltons.cacheutils import LRI, LRU, cached

# Persistent LRU cache for the parts of speech
cached_data = shelve.open('cached_data', writeback=True)  1
atexit.register(cached_data.close)  2

# Retrieve or create the "parts of speech" cache
cache_POS = cached_data.setdefault(
    'parts_of_speech', LRU(max_size=5000))  3

@cached(cache_POS)  4
def part_of_speech(word):
    items = vb.part_of_speech(word.lower())
    if items:
        return json.loads(items)[0]['text']

# Temporary LRI cache for word substitutions
cache = LRI(max_size=30)

@cached(cache)  5
def synonym(word):
    items = vb.synonym(word)
    if items:
        return choice(json.loads(items))['text']

@cached(cache)  5
def antonym(word):
    items = vb.antonym(word)
    if items:
        return choice(items['text'])

for raw_word in blank_space.strip().split(' '):
    if raw_word == '\n':
        print(raw_word)
        continue
    alternate = raw_word  # default is the original word.
    # Remove punctuation
    word = raw_word.translate(
        {ord(x): None for x in punctuation})
    if part_of_speech(word) in ['noun', 'verb',
                                'adjective', 'adverb']:  6
        alternate = choice((synonym, antonym))(word) or raw_word
    print(alternate, end=' ')


```


boltons.iterutils.chunked_iter(src, size)



```
>>> list(windowed_iter(range(7), 3))
[(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]

```

## boltons.fileutils.AtomicSaver 

Context manager helps to make sure that file-writes are protected against corruption. It achieves this by writing file data to temporary, or intermediate files, and then using an atomic renaming function to guarantee that the data is consistent. This is particularly valuable if there are multiple readers of a large file, and you want to ensure that the readers only ever see a consistent state, even though you have a (single!) writer changing the file data.

## boltons.debugutils.pdb_on_signal()

**slugify()**: modify a string to be suitable, e.g., for use as a filename, by removing characters and symbols that would be invalid in a filename.





