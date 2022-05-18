
# 字符串拼接

# 方式1 逗号
str_a = 'python'
print('hello', str_a, '!')


# 方式2
str_b = 'It is summer ' 'of 2019!'
print(str_b)


# 方式3
str_c = 'Love makes ' \
        'man grow up ' \
        'or sink down!'
print(str_c)


# 方式4

str_d = 'string'
str_e = 'demo'
print(str_d + str_e)
str_e += str_d
print(str_e)


# 方式5
str_f = 'a_' * 10
print(str_f)

# 方式6
# %s,%d,%f的作用是占位作用，然后在字符串后面跟一个%，再在后面写拼到占位位置的内容。
# %s:将一个字符串拼接到前面的字符串中
# %d:将一个整型数字转换成字符串拼接到前面的字符串中，可以设置整数的位数，前面补0
# %f:将一个浮点型数字转换成字符串拼接到前面的字符串中，可以设置小数点后的位数，后面补0

str_g = 'aaaaaaaaaaaa%saaaaaaaaa' % 'A'
print(str_g)
str_h = 'aaaaaaaaaaaa%06daaaaaaaaa' % 10
print(str_h)
str_i = 'aaaaaaaaaaaa%.03faaaaaaaaa' % 0.77
print(str_i)


# 方式7
str_j = 'python {}! format {}!'.format(666, 999)
print(str_j)


# 方式8、通过str.join()方法拼接
list_l = ['生', '如', '夏', '花', '之', '绚', '烂', '，', '死', '如', '秋', '叶', '之', '静', '美', '！']
str_l = ''.join(list_l)
print(str_l)
tuple_m = ('生', '如', '夏', '花', '之', '绚', '烂', '，', '死', '如', '秋', '叶', '之', '静', '美', '！')
str_m = '-'.join(tuple_m)
print(str_m)


# 方式9 通过string模块中的Template对象拼接
from string import Template
t = Template('${s1} ${s2}!')
str_n = t.safe_substitute(s1='Hello', s2='Python')
print(str_n)

# 方式10
o = 6666666666
p = 7777777777
str_o = f'Python {o} hello {p} !'
print(str_o)