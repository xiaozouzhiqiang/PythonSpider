import re
#===================#
# 验证手机号码
# text = "18565458658"
# ret = re.match('1[34578]\d{9}',text)
# print(ret.group())

# 验证邮箱
# text = 'xiaozouzhiqiang@gmail.com'
# ret = re.match('\w+@[a-z0-9]+\.[a-z]+',text)
# print(ret.group())

# 验证URL
# text = "http://www.baidu.com/zouzhiqiang"
# ret = re.match('(http|https|ftp)://[^\s]+',text)
# print(ret.group())

# 验证身份证号码
# text = "125455412554455111"
# ret = re.match('\d{17}[\dxX]',text)
# print(ret.group())

# 匹配0-100之间的数字

text = "19"
ret = re.match('[1-9]\d?$|100$',text)
print(ret.group())