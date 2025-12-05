import re

pat = r"Rs.[0-9]+"
l2 = "The orange costs Rs.23 and Grapes costs Rs.670"

print(re.findall(pat,l2))