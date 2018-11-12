#!/usr/bin/env python3.6
'''
yield from的使用
1）为了让生成器（带yield函数），能简易的在其他函数中直接调用，就产生了yield from。
2）以下代码，htest为生成器，itest通过yield from 直接调用htest。这样itest也变成了一个生成器。
创建itest实例不断的去获取数据，当生成器执行结束时，会抛出StopIteration异常。那这个异常是htest抛出的，
还是itest抛出的。通过捕获异常，会发现其实是itest抛出异常，htest并不会抛出StopIteration异常。
3)yield from 也可以返回值，通过变量接收。
变量接收的值，即htest使用return返回的值。
示例代码中，当i==3时，会直接使用return返回，这时val的值就是100；
因为htest函数中不是使用yield返回值，所以itest会继续执行print(val)语句。
itest代码执行完，然而并没有使用yield返回数据（htest中没有，itest中也没有），
所以马上会抛出StopIteration异常)(如果在itest函数最后使用yield返回一个数据，就不会抛出异常)。

---------------------
作者：chenbin520
来源：CSDN
原文：https://blog.csdn.net/chenbin520/article/details/78111399
版权声明：本文为博主原创文章，转载请附上博文链接！

'''

def htest():
    i = 1
    while i < 4:
        s = yield i
        print("s : ",s)
        if i == 3:
            return 100 # 调用next 执行到下一个yield，如果使用return，会抛出错误
        i += 1

def itest():
    # itest 调用 htest生成器， itest也变为生成器
    val = yield from htest()
    print(val)

t = itest()
t.send(None)
print(t)
j = 0
while j < 3:
    j += 1
    try:
        rr =t.send(j)
        print("rr :",rr)
    except StopIteration as e:
        print('异常了')

g = htest()
print(g)


r =g.send(None)
print("r: ",r)


r =g.send(1)
print("r: ",r)


r =g.send(2)
print("r: ",r)


# r =g.send(3)
# print("r: ",r)




