tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]
def lngest(inrlst):
    u = 0
    for i in range(len(inrlst)):
        if len(inrlst[i]) > u:
            u = len(inrlst[i])
    return u

#print(lngest(tableData[0]))
for i in range(len(tableData[0])):
    for u in range(len(tableData)):
        print(tableData[u][i].rjust(lngest(tableData[u])),end=" ")
    print()