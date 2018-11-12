#!/usr/bin/env python3.6
'''
    yield from
    调用yield from 将gen 变为生成器

'''
def gen():
    yield from ["x","y","z"]
for i in gen():
    print(i)