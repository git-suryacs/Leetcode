from collections import OrderedDict

d = OrderedDict()
d[1] = 2
d[2] = 3
d[3] = 4

for k,v in d.items():
    print(k,v)

print(d.popitem(last=False))
print(d.popitem())