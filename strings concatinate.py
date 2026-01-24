a="hello"
b= "world"
c= a+" " +b
print(c)

d = 30
e=f"i'm {d}"

x=16
y=f"i'm sweet {x}"
print(y)

a= 40
b=3
c="total ammount {}"
#print(f"total ammount {}")
print(c.format(a+b))

print(f"price {3*4}")
x=4
print(f"the price is {x:.4f}")

txt= "we are so' called \"vikings\" from the north"
print(txt.lstrip())