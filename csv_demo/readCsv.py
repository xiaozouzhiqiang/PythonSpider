import csv

# 直接读取
with open('test.csv','r')as fp:
    # reader是一个迭代器
    reader = csv.reader(fp)
    next(reader)
    for text in reader:
        print(text)
        # name = text[-1]
        # print(name)
# 将csv读取为字典格式
with open('test.csv','r') as fp:
    # 使用DictReader创建的reader对象
    # 不会包含标题哪行的数据
    # reader是一个迭代器，遍历这个迭代器，返回的是一个字典
    ditReader = csv.DictReader(fp)
    for dtext in ditReader:
        print(dtext)
        value = {"id":dtext['id'],'name':dtext['name']}
        print(value)
