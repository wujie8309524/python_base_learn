yield 与 yield from
===
```python
#!/usr/bin/env python3.6
'''
对于普通的生成器，第一个next调用，相当于启动生成器，会从生成器函数的第一行代码开始执行，直到第一次执行完yield语句（第4行）后，跳出生成器函数。

然后第二个next调用，进入生成器函数后，从yield语句的下一句语句（第5行）开始执行，然后重新运行到yield语句，执行后，跳出生成器函数，
---------------------
作者：pfm685757
来源：CSDN
原文：https://blog.csdn.net/pfm685757/article/details/49924099
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
def consumer():
    r = ' here'
    for i in range(3):  # i : 0 , 1 , 2
        yield r
        r = '200 ok ' + str(i)
    return "done"


cc = consumer()
# 如果使用next方式，还需要捕捉 StopIteration 错误才能拿到最后return的值
while True:
    try:
        nn = next(cc)
        print("n is :",nn)
    except StopIteration as e:
        print("last n is :",e.value)
        break
print('\n\r')
#  防止 StopIteration 超出边界错误 用for 循环代替 next 取不到最后return的值
c1 = consumer()
for cc1 in c1:
    print(cc1)


c = consumer()

# 第一次执行next 启动生成器，执行到yield行，返回r
n1 = c.__next__()  #  执行完 next 悬停  0  循环体的yield r 处
print(n1)          #  here

# 第二次执行next，生成器从yield下一行开始执行，循环到yield r 返回
n2 = c.__next__()  #  执行完 next 悬停在 1  循环体的yield r 处
print(n2)          # 200 ok 0

# 第三次执行next，生成器从yield下一行开始执行，循环到yield 人返回
n3 = c.__next__()  #  执行完 next 悬停在 2  循环体的yield r 处
print(n3)          # 200 ok 1

n4 = c.__next__()  #  执行完 next 寻找 3 循环体 yield r 失败 超出范围
print(n4)          # 200 ok 2
```



```python

#!/usr/bin/env python3.6
'''
了解了next()如何让包含yield的函数执行后，我们再来看另外一个非常重要的函数send(msg)。
其实next()和send()在一定意义上作用是相似的，区别是send()可以传递yield表达式的值进去，
而next()不能传递特定的值，只能传递None进去。因此，我们可以看做c.next() 和 c.send(None) 作用是一样的。
需要提醒的是，第一次调用时，请使用next()语句或是send(None)，不能使用send发送一个非None的值，否则会出错的，
因为没有Python yield语句来接收这个值。
下面来着重说明下send执行的顺序。当第一次send（None）（对应11行）时，
启动生成器，从生成器函数的第一行代码开始执行，直到第一次执行完yield（对应第4行）后，
跳出生成器函数。这个过程中，n1一直没有定义。

下面运行到send（1）时，进入生成器函数，注意这里与调用next的不同。
这里是从第4行开始执行，把1赋值给n1，但是并不执行yield部分。下面继续从yield的下一语句继续执行，然后重新运行到yield语句，
执行后，跳出生成器函数。
---------------------
作者：pfm685757
来源：CSDN
原文：https://blog.csdn.net/pfm685757/article/details/49924099
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
def consumer():
    r = 'here'
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    aa = c.send(None)
    print("aa :",aa)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
```

```python
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

```

```python
#!/usr/bin/env python3.6
'''
    yield from
    调用yield from 将gen 变为生成器

'''
def gen():
    yield from ["x","y","z"]
for i in gen():
    print(i)


```