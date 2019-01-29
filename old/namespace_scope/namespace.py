#Höfundur: Huginn Þór Jóhannsson
'''
a=2
print("id(a)=",id(a))
a +=1
print("id(a)=",id(a))
print("id(3)=",id(3))
b=2
print("id(2)=",id(2))
print("id(b)=",id(b))
'''
def outer():
    global a
    a=20
    def inner():
        global a
        a=30
        print(a)
    inner()
    print("a=",a)
a=10
outer()
print("a=",a)
