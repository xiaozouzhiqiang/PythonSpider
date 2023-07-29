import re
# text = "apple price is $299"
# ret = re.search("\$\d+",text)
#
# # 原生字符串
# text = r'\n'

text = "\\n"
ret = re.match('\\\\n',text)


# 分组
text = "apple price is $99, orange is $21"
ret = re.search(r".*(\$\d+).*(\$\d+)",text)
print(ret.group())