# _*_ coding: utf-8 _*_
def trim(s):
    if len(s) == 0:
        return ''
    if s[0] != ' ':
        if s[-1] != ' ':
            return s
        else:
            s = s[:-1]
            return trim(s)
    else:
        s = s[1:len(s)]
        return trim(s)
trim(' a')


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim(' ') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
