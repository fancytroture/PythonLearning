###special message
name = "eric"
language = "python"
message = f"Hello {name.title()}, would you like to learn some {language.title()} today.  "
print(f"{message.strip()}")

###adjust name
name = "zuo xin"
print(f"{name.title()}")
print(f"{name.upper()}")
print(f"{name.lower()}")

###famous sentences
name = "zuo xin"
sentence = "bao bao du du da lei lei"
print(f"{name.title()} once said, '{sentence}'")

###famous sentences plus
name = "zuo xin"
sentence = "bao bao du du da lei lei"
message = f"{name.title()} once said, '{sentence}!'"
print(message)

###name empty
name = "\tzuo  \n\txin "
print(f"{name.rstrip()}")
print(f"{name.lstrip()}")
print(f"{name.strip()}")

###removesuffix
name = "zuoxin.txt"
print(f"{name.removesuffix('.txt')}")
