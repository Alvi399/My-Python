mystack:list = []
mystack2 = []

if type(mystack) == type(mystack2):
    print("Deklarasi menghasilkan tipe sama")

for i in range(10):
    mystack.append(i)
print(mystack)
mystack.pop()
print(mystack)
