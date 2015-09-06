import UF

print('hello')
with open('numbers', 'r') as f:
    arr = [[int(x) for x in line.split()] for line in f]

# for pair in arr

uf = UF.UF(10)
for pair in arr:
    if not uf.connected(pair[0], pair[1]):
        uf.union(pair[0], pair[1])

uf.print()
# print(arr)
