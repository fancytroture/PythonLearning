##循环
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

##Conbination
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, it is a good trick")

##Conbination
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, it is a good trick.\n"
          f"I am waiting for the next trick, {magician.title()}.\n")
