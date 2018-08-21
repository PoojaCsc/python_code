import re

text = "My name is Pooja"
matches = re.findall("\w-", text)
print(matches)
print(len(matches))