fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
#print(len(fruits))
#print(fruits.count('apple'))
(fruits.sort(reverse=False))
print(fruits)

#this was't required , we could add an element using append only
def addElement(x, mylist = []):
   mylist.append(x)
   return mylist


#Implementing FIFO
def popQueue(list):
    list.pop(0)
    return list

#This was also not required, could have tested with the fruits list only but anyways
def implementQueue():
    first_queue = []
    first_queue = addElement(1, mylist=[])
    second_queue = addElement(2, first_queue)
    return  second_queue



output = implementQueue()
print(output)

output = addElement(3,mylist=output)
print(output)
output = popQueue(output)
print(output)


