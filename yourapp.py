# the quick brown fox jumps over the lazy dog
import operator
from collections import defaultdict

from pip._vendor.distlib.compat import raw_input

d = defaultdict(int)
text = str(raw_input(""))
for w in text.split():
    d[w] += 1
for w in sorted(d, key=d.get(1), reverse=True):
    print(w, d[w])
print('\n')
for w in sorted(d, key=d.get(1), reverse=False):
    print(w, d[w])
