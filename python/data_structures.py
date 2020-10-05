print("Hello World")
#list
animals = ["tiger", "bear", "lion", "panda", "elephant"]
for x in animals:
    print(x)
print(animals)

print(animals[0])

animals[0] = "dog"
print(animals)
#list methods
fruits = ["berries", "apples", "grapes", "oranges"]
vegetables = ["kale", "broccoli", "lettuce"]

fruits.extend(vegetables)
print(fruits)

vegetables.append("beans")
print(vegetables)

vegetables.sort()
print(vegetables)

vegetables.sort(reverse=True)
print(vegetables)

print(fruits.count("berries"))

print(fruits.index("grapes"))

fruits.insert(0,"banana")
print(fruits)

fruits.pop()
print(fruits)

vegetables.remove("kale")
print(vegetables)
#nested lists
fruitlist = [["apples", "berries", "kiwi"],
             ["oranges", "berries", "plums"],
             ["mangoes", "bananas", "coconuts"],
             ["pineapples"]
             ]
print(fruitlist[1][1])

for row in fruitlist:
    for col in row:
        print(col)
#tuples
animals = tuple(("lion", "tiger", "bear"))
print(animals)
#sets
fruitset = {"grapes", "apples", "berries"}
for x in fruitset:
    print(x)
animalset = (("lion", "tiger", "bear"))
print(len(animalset))

fruitset.add("oranges")
print(fruitset)
fruitset.update(["mangoes", "kiwi"])
print(fruitset)
fruitset.remove("kiwi")
print(fruitset)
#dictionary
mycar = {
    "brand":"Range Rover Sports",
    "model":"HSE",
    "year":2020
}
print(mycar)

mygreens = dict(fruit="green apples", vegetables="kale")
print(mygreens)

print(len(mycar))
mycar["year"]=2021
print(mycar)

mycar.update({"color":"silver"})
print(mycar)

print(mycar.keys())