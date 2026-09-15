import random
lo = ["hi","hello","welcome"]
ra = random.choice(lo)
va = input("hello ")
v1 = va.upper
v2 = va.lower
if v1 == "hi" or v2 == "welcome" or va == "welcome":
    print(ra)
elif va == "what":
    print(va)
else:
    print("error")
l = [1,3,6]
print(min(l[2],l[1],l[0]))