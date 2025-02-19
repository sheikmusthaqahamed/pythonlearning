data={1:"Hi",-3:"Bye2",-3:"Bye1"}

# print(data[3])

print(data.get(3,"Dei"))

data.setdefault("dd","ji")

print(tuple(data.items()))
print(type(data.keys()))
print(type(data.values()))
print(type(data.items()))
print(type(list(data.items())))

for key,value in data.items():
    print(key,value)

stro = "Sheik"
sheik=stro.casefold()
print(sheik)
