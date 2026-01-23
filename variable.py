x =str(3)
y = int(3)
z = float(3)

a = 5
b = "upo"
#print(type(a))

i,j,k = 5,7,8
#print(k)

x=y=z='orange'
#print(y)


fruits=['apple','banana','cherry']
x,y,z= fruits
#print(z)


x = "awesome"
def fun():
    global x
    x = 'funny '+x
    print(x)
fun()