#if
a=7
b=8
c=9
if a<b:
    print(a,"is smaller than",b)
elif b>=c:
    print(b,"is smaller than",c)
else:
    print(c,"is larger than",b,"and",a)

#while
i=1
while i<7:
    print(i)
    i+=1

#for loop
fruits=["grapes", "oranges", "berries"]
for x in fruits:
    print(x)

#nested loop
fruitss=["apples", "banana", "berries"]
colors=["green", "yellow", "purple"]
for x in colors:
    for y in fruits:
        print(x,y)

#continue
i=0
while i<8:
    i+=1
    if i==4:
        continue
    print(i)

#break
i=1
while i<8:
    print(i)
    if i==3:
        break
    i+=1

