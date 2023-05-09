import re

txt = "xyxz abbababababababa bbzy ababa"

#Check if the string has other characters than a, r, or n:

l1 = re.findall("a[a|b]*a", txt)
l2 = re.findall("a[a|b]*a", txt)
blank = re.findall("a[a|b]*a", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
