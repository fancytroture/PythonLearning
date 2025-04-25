##sort command
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

###reverse = True
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort(reverse=True)
print(cars)

##sorted()不影响原列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(sorted(cars,reverse=True))
cars.sort(reverse=True)
print(cars)

##len()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
