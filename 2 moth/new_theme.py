import re

text = "Email: +996555550145"
pettern = r".\d+"

result = re.findall(pettern,text)
print(result)