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
