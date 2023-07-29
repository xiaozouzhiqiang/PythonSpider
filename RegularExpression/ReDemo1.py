import re

# 匹配某个字符串
# 如果出现《没有类型》的错误，并不是代码中出现错误，而是match方法，只能聪哥第一个字符开始查找
text = "Hello World"
ret = re.match('Hello', text)

# .匹配任一字符，但是不能匹配到换行符
text = "Hello World"
ret = re.match('.', text)

# 匹配任一数字
textnum = "123456"
retnum = re.match('\d', textnum)

# 匹配任一非数字
textnum = "s125"
retnum = re.match('\D', textnum)


# 匹配任一空白字符，包括\n  \t 等
textnum = " "
retnum = re.match('\s', textnum)


# 匹配a-z 和 A-Z 以及数字, \W则相反
textnum = "a45451"
retnum = re.match('\w', textnum)


# 还可以用中括号的方式来表达
# \d : [0-9]
# \D : 0-9
# \w : [0-9a-zA-Z]
# \W : [^0-9a-zA-z]

# 举个例子
text = "a45451"
retnum = re.match('[0-9a-zA-Z]', text)
print(retnum.group())
