str = input('enter string to sort: ')
lst = []
for char in range(len(str)):
    lst.append(str[char])
sortedLst = []
lst.sort(reverse=True)
sortedLst = sorted(lst, reverse=True, key=lambda c:lst.count(c))
print("".join(sortedLst)) 