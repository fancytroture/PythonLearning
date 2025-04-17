###title
name = "ada lovelace"
print(name.title())

###upper and lower
print(name.upper())
print(name.lower())

###combine
firstname = "ada"
lastname = "lovelace"
full_name = f"{firstname} {lastname}"
print(full_name)

###f_combine
firstname = "ada"
lastname = "lovelace"
full_name = f"{firstname} {lastname}"
print(f"Hello, {full_name}!")

firstname = "ada"
lastname = "lovelace"
full_name = f"{firstname} {lastname}"
print(f"Hello, {full_name.title()}!")

###\t and \n usage
print("python")
print("\tpython")

print("zuoxin I love you")
name = "zuo xin"
print(f"{name.title()}\nI\nlove\nyou\n")

###combination \t and \n
message = "zuoxin \n\tI\n\tlove\n\tyou\n\t!"
print(f"{message.title()}")

###find empty—— rstrip and lstrip
mylover = " zuoxin "
print(f"{mylover.rstrip()}")
print(f"{mylover.lstrip()}")
print(f"{mylover.strip()}")

###removeprefix
mylover = "little white xinxin zuo xin"
name = f"{mylover.removeprefix('little white xinxin ')}"
print(f"{name.title()}")