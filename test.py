# types
# count
# sum of elements 
# product of elements


# DATA TYPES:
# list:
a = ['fazal',[1,2,3,40],[0,1,2,3],(1,2)]
count = 0
for s in a:
    if type(s) == list:
        count += 1
print(count)

#set:
a = [{1,2,3},{10,20,30},['fazal','apple'],10, 0.4]
count = 0
for i in a:
    if type(i) == set:
        count += 1
print(count)

# tuple:
z = [(2,4,6),(1,3,5),(3,5,7,11),10,30,15,1.9]
count = 0
for a in z:
    if type(a) == tuple:
        count += 1
print(count)


# integers:
c = [1, 2, 3, 'fazal', 0.2, 19, 2]
count = 0
for d in c:
    if type(d) == int:
        count += 1
print(count)

# float:
b = [1.9, 10.2, 'fazal', 74, 1.3, 1.4]
count = 0
for c in b:
    if type(c) == float:
        count += 1
print(count)

# bool:
k = [1,True, 0.4, False, 9, 26]
count = 0
for l in k:
    if type(l) == bool:
        count += 1
print(count)


# sum:
a = [1,3,5,7,10]
sum = 0
for f in a:
    sum += f
print(sum)


# product:
j = [2,4,6,8]
product = 1
for l in j:
    product *= l
print(product)


# length:
a = [11, 20, 67, 2.8, 1.3, "fazal", [1,2],{10,20}]
sum = 0
for i in a:
    sum += 1
print(sum)