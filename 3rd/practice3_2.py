##invitation
list = ['kobe', 'curry', 'messi']
print(f"Hello {list[0].title()}, {list[1].title()} and {list[2].title()}, \
I would like to invite you to have a dinner.")

##del and append
list = ['kobe', 'curry', 'messi']

miss_person = list.pop(0)
print(f"{miss_person.title()}")
list.insert(0,'joker')
print(list)

#miss_person = list[0]
#print(miss_person)
#list[0]=joker
#print(list)

print(f"Hello {list[0].title()}, {list[1].title()} and {list[2].title()}, \
I would like to invite you to have a dinner.")

##A larger desk
list = ['kobe', 'curry', 'messi']

miss_person = list.pop(0)
print(f"{miss_person.title()}")
list.insert(0,'joker')
print(list)

list.insert(0,'mama')
list.insert(2,'zuoxin')
list.append('durant')

#miss_person = list[0]
#print(miss_person)
#list[0]=joker
#print(list)

print(f"Hello {list[0].title()}, I would like to invite you to have a dinner.")
print(f"Hello {list[1].title()}, I would like to invite you to have a dinner.")
print(f"Hello {list[2].title()}, I would like to invite you to have a dinner.")
print(f"Hello {list[3].title()}, I would like to invite you to have a dinner.")
print(f"Hello {list[4].title()}, I would like to invite you to have a dinner.")
print(f"Hello {list[5].title()}, I would like to invite you to have a dinner.")

##Shorten the list
list = ['kobe', 'curry', 'messi']

miss_person = list.pop(0)
print(f"{miss_person.title()}")
list.insert(0,'joker')
print(list)

list.insert(0,'mama')
list.insert(2,'zuoxin')
list.append('durant')

#miss_person = list[0]
#print(miss_person)
#list[0]=joker
#print(list)

print(f"Hello {list[0].title()}, I would like to invite you to have a dinner.")
print(f"Hello {list[1].title()}, I would like to invite you to have a dinner.")
print(f"Hello {list[2].title()}, I would like to invite you to have a dinner.")
print(f"Hello {list[3].title()}, I would like to invite you to have a dinner.")
print(f"Hello {list[4].title()}, I would like to invite you to have a dinner.")
print(f"Hello {list[5].title()}, I would like to invite you to have a dinner.")
print("I am sorry to tell you that I can only invite two guests due to limited dishes.")
popped_person = list.pop()
print(f"I am very sorry, {popped_person.title()}.")
popped_person = list.pop()
print(f"I am very sorry, {popped_person.title()}.")
popped_person = list.pop()
print(f"I am very sorry, {popped_person.title()}.")
popped_person = list.pop(1)
print(f"I am very sorry, {popped_person.title()}.")
print(list)
print(f"{list[0].title()}, you are still invited!")
print(f"{list[1].title()}, you are still invited!")
del list[0]
del list[0]
print(list)