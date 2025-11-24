l = [1,2,3,4,5]
l.append(8)
print(l)
print(type(l))

r = [2,4,6,8]
r.extend([10,5])
print(r)
print(type(r))

a = [1,8,6,4]
a.insert(2,4)
print(a)

fazal= [10, 20, 30, 40]
fazal.remove(30)
print(fazal)
print(type(fazal))

all = [1,2,3,4,5]
print(all.clear())

z = [2, 4, 6, 10, 8, 10]
print(z.count(10))

_fazal = [1,3,5,7]
print(_fazal.copy())

f = [3, 5, 7, 9, 11]
print(f.sort())

s = [2, 3, 4, 5, 6]
s.reverse()
print(s)

# check the data types of list.

l = ['fazal', 10.2, 50, [1, 2, 3], (4, 5)]
for z in l:
    print(z, type(z))

# count of str:

a =['apple', 10, [10, 20], 55, 'banana', 1.3, 'cherry']
count = 0
for z in a:
    count += 1
print(count, type(z))

a = ['apple', 10, [10,20], 55, 'banana', 1.3, 'cherry']
count = 0
for i in a:
    if type(i) == str:
        count += 1
print(count)

# check if number is odd or even:

num = 20
if num % 2 == 0:
    print('Even')
else:
    print('Odd')


# check count of odd and even numbers in list:

l = [5, 8, 10, 11, 4, 15]
even_count = 0
odd_count = 0

for n in l:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers:",even_count)
print("Odd numbers:", odd_count)

# sum of all elements in list:

p = [1, 2, 3, 4, 5, 6]
total = sum(p)
print(total)

# product of all elements in list:

l = [1, 3, 5, 7, 10]
product = 1
for p in l:
  product *= 1
print(product)    

# integer:
a = [10, 'fazl', 20, 's', 30, 0.6, 'q', 14]
count = 0
for b in a:
    if type(b) == int:
        count += 1
print(count)

# float:
_a= [10, 'fazl', 20, 10.2, 30, 0.6, 'q', 15.5, 20.3]
count = 0
for c in _a:
    if type(c) == float:
        count += 1
print(count)

# list:
l = [[10,1,4,3],[5,6,4.5,3,2],[1,2.5,7,3],(10,20),5.3,40]
count = 0
for k in l:
    if type(k) == list:
        count += 1
print(count)

# set:
a = [{1,2},'z',(10,3),10,{'fazal'},True]
count = 0
for i in a:
    if type(i) == set:
        count += 1
print(count)

#tuple:
q = [(1,2,3),10,20,(3,4,5),'python',(20,30,49),5.5]
count = 0
for r in q:
    if type(r) == tuple:
        count += 1
print(count)

#bool:
a = [True, 10, 20, False, 0.1, 'ball']
count = 0
for j in a:
    if type(j) == bool:
        count += 1
print(count)

#length:
a = [3,4,5,6,7,'apple','cherry','cat',10.3,[12,34,56]]
sum = 0
for b in a:
    sum += 1
print(sum)

r = [50,20,39,'fazal',1.5,1.9,[10,11,12,13]]
print(len(r))

r = [1,2,3,4,5,6]
sum  = 0
for s in r:
    sum += s
print(sum)

r = [1,2,3,4,5,6]
product = 1
for s in r:
    product *= s
print(product)