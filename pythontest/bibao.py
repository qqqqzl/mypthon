def fun(s):
    return len(s)
print('***********   fun info .........')
print(id(fun))
print(type(fun))
print(fun)

print('**********    a info .........')
a=fun
print(id(a))
print(type(a))
print(a)

print('**********   l[0] info .........')
l=[]
l.append(fun)
print(id(l[0]))
print(type(l[0]))
print(l[0])

def useFun(fun1):
    print(id(fun1))
    print(type(fun1))
    print(fun1)
    return fun1

print('*******  use Fun  ***********')
a = useFun(fun)
print(id(a))
print(type(a))
print(a)


######  另外说明下函数的 __call__
print('****   test Class __call__   ******')
class Add():
    def __init__(self, n):
        self.n = n 
    def __call__(self, x):
        return self.n + x

print('^^^^^^^^   ADD  ^^^^^^^^^^^^^')
print(id(Add))
print(type(Add))
print(Add)

ad = Add(10)
print(id(ad))
print(type(ad))
print(ad)

ad = Add(20)
print(id(ad))
print(type(ad))
print(ad)

a = ad
print(id(a))
print(type(a))
print(a)
        
########   闭包 ##############
print('^^^^^^    闭包    ^^^^^^^^')
def print_msg():
    # print_msg 是外围函数
    msg = " qu ni mei "
    def printer():
        # printer 是嵌套函数
        print(msg)
    print('@@@@@   Inner printer @@@@@@')
    print(id(printer))
    print(type(printer))
    print(printer)
    return printer

another = print_msg()
# 输出 zen of python
print('@@@@@  Outer another @@@@@')
print(id(another))
print(type(another))
print(another)
another()


#####   闭包的属性  #########
print('^^^^  闭包的属性 ^^^^^^^')
def adder(x):
    z=10
    l=[1,2,3]
    def wrapper(y):
        return x + y +z + l[0]
    return wrapper

adder5 = adder(5)
print(adder.__closure__)
print(adder5.__closure__)
#print(type(adder5.__closure__)
print('这个闭包的内容的长度 = ',len(adder5.__closure__))
for i in range(0,len(adder5.__closure__)):
    print('adder5.__closure__[',i,']',adder5.__closure__[i].cell_contents)
# 输出 15
#adder5(10)
# 输出 11
#adder5(6)

#######   源代码研究   ########
print(' ^^^^^^   源代码研究 ^^^^^^^^')
def f(x):
    print("f co_cellvars:"+"".join(f.__code__.co_cellvars)) # f co_cellvars:x  
    print("f co_freevars:"+"".join(f.__code__.co_freevars)) # f co_freevars:  
    def add(value):
        return x+value  
    print("add co_cellvars:"+"".join(add.__code__.co_cellvars)) # add co_cellvars:  
    print("add co_freevars:"+"".join(add.__code__.co_freevars)) # add co_freevars:x  
    return add  
