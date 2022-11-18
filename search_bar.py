n = int(input())
poisks = list()
searchs = list()
for i in range(n):
    poisk = input()
    poisks.append(poisk)
nn = int(input())
for i in range(nn):
    search = input()
    searchs.append(search)
for i in range(n):
    for j in range(nn):
        if search[i] in poisks[j]:
            print(search[j])
