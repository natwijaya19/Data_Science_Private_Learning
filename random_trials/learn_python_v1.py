# %%
l = [1, 2, 3, 4]
for item in map(lambda n: n * 2, l):
    print(item)

# %%
l = [1, 2, 3, 4]
for item in filter(lambda n: n < 4, l):
    print(item)

# %%
l = [1, 2, 3, 4]
for item in l:
    result = item * 2
    print(result)

# %%
import decimal as dc

a = dc.Decimal(1)
b = dc.Decimal(0.9)
c = a - b
print(c)

# %%
d = c == 0.1
print(d)
# %%
e = 1-0.9
# %%
d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
print(sorted(d, key= None, reverse = True))
print(sorted(list(d.values())))

# %%
def wordcount(fname):
    try:
        fhand = open(fname, 'r')
    except:
        print('File can not be opened')
        exit()

    count = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    return count


count = wordcount('alice.txt')

filtered = {key: value for key, value in count.items() if 20 > value > 18}

print(filtered)

# %%s
clear
