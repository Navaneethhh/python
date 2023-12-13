s = input()
if s[-3:] == "ing":
    a =s+"ly"
    print(a)
else:
    b = s[-3:]
    c = s.replace(b, "ing")
    print(c)
