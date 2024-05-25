# Tuple method
#count():
#1
tuple=(2,4,5,6,2,3,4,4,7)
count=tuple.count(4)
print(count)

#2
my_tuple=('a',1,'f','a',5,'a')
print(my_tuple.count('a'))

#index():
my_tuple=('a',1,'f','a',5,'a')
print(my_tuple.index('f'))

#len():
my_tuple=('a',1,'f','a',5,'a')
print(len(my_tuple))

#max():
tuple=(2,4,5,6,2,3,4,4,7)
x=max(tuple)
print(x)

#min():
tuple=(2,4,5,6,2,3,4,4,7)
x=min(tuple)
print(x)

#sum():
tuples=(2,4,6,8,10)
total=sum(tuples)
print(total)

#sort():
animals=("cat","lion","eagle","bear","horse")
animals=sorted(animals)
print(animals)

#loop tuple
list_of_tuples=[]
for i in range(5):
    a_tuple=(i,i+1)
    list_of_tuples.append(a_tuple)
print(list_of_tuples)

#del():
x=(2,4,6,8,10)
print(x)
del(x)
print(x)