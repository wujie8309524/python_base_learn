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