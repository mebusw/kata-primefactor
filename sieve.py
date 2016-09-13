# !encoding=utf8
# primes = filterPrime [2..] 
#   where filterPrime (p:xs) = 
#           p : filterPrime [x | x <- xs, x `mod` p /= 0]

# filterPrime 相当于一个函数 
# p:xs, p 是列表的第一项，xs是剩余部分
# [x | x <-xs, x `mod` p /=0] 是列表生成式，好像python里也有类似的写法
# 把xs，即剩余列表中，不被p整除的数字放入列表
# 展开等于
# 2 : 不被2整除数列上筛选
#     -> 3 : 被2筛过后，不被3整除数列 筛选
# ……
# 虽然是无限列表，但是每次取到第一个值p后就可以停止，所以能够惰性求值          


from pipe import *
from pipe import itertools

## Unlimited Sequence
def primes(xs):
    while 1:
        p = next(xs)
        yield p
        xs = (lambda xs, p: (x for x in xs if x % p != 0))(xs, p)

print primes(itertools.count(2)) | take(25) | as_list

## Limited Sequence
def rc(s):
    return [s[0]] + rc([x for x in s[1:] if x % s[0] != 0]) if len(s) > 1 else []

print rc(range(2, 103))
